import requests
import json
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv
import os

class ShopifyStore():

    def __init__(self):
        load_dotenv()
        self.access_token = os.environ.get("SHOPIFY_API_KEY")
        self.password = os.environ.get("SHOPIFY_API_PASSWORD")
        self.shop_url = os.environ.get("SHOPIFY_SHOP_NAME")
        self.api_version = os.environ.get("SHOPIFY_API_VERSION", "2023-10")

    def get_collections_data(
        self,
        handles: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Obtiene los datos de las colecciones de la tienda en el formato especificado.
        
        Args:
            shop_url: URL de la tienda (ej: 'tu-tienda.myshopify.com')
            access_token: Token de acceso de la API de Shopify
            handles: Lista opcional de handles de colecciones a incluir
            exclude: Lista opcional de handles de colecciones a excluir
            
        Returns:
            Diccionario con la lista de colecciones en el formato especificado
        """
        
        # Construir la consulta GraphQL
        query = """
        query getCollections($first: Int!, $query: String) {
            collections(first: $first, query: $query) {
                edges {
                    node {
                        id
                        handle
                        title
                        description
                        seo {
                            title
                            description
                        }
                        productsCount {
                            count
                        }
                        updatedAt
                    }
                }
                pageInfo {
                    hasNextPage
                    endCursor
                }
            }
        }
        """

        search_query = ""
        if handles:
            handle_queries = [f"handle:{handle}" for handle in handles]
            search_query = " OR ".join(handle_queries)

        # Variables para la consulta
        variables = {
            "first": 250,
            "query": search_query if search_query else None
        }
        
        return self._send_request(query, variables, objects="collections", exclude=exclude)


    def get_products_data(
        self,
        handles: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Obtiene los datos de los productos de la tienda en el formato especificado.
        """
        query = """
            query getProducts($first: Int!, $query: String) {
            products(first: $first, query: $query) {
                edges {
                node {
                    id
                    handle
                    title
                    description
                    vendor
                    productType
                    tags
                    collections(first: 10) {
                    edges {
                        node {
                        handle
                        }
                    }
                    }
                }
                }
            }
            }
        """

        search_query = ""
        if handles:
            handle_queries = [f"handle:{handle}" for handle in handles]
            search_query = " OR ".join(handle_queries)

        variables = {
            "first": 250,
            "query": search_query if search_query else None
        }

        return self._send_request(query, variables, objects="products", exclude=exclude)



    def _send_request(self, query: str, variables: dict, objects: str, exclude: Optional[List[str]] = None):
        # Headers para la petición
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': self.access_token
        }
        
        # URL del endpoint GraphQL
        graphql_url = f"https://{self.shop_url}/admin/api/{self.api_version}/graphql.json"
        
        all_objects = []
        has_next_page = True
        cursor = None
        
        # Construir filtro de búsqueda si se especifican handles

        while has_next_page: 
            # Si hay cursor para paginación, modificar la consulta
            if cursor:
                query_with_cursor = query.replace(
                    f"{objects}(first: $first, query: $query)",
                    f"{objects}(first: $first, query: $query, after: $after)"
                )
                variables["after"] = cursor
                current_query = query_with_cursor
            else:
                current_query = query
            
            # Realizar la petición
            response = requests.post(
                graphql_url,
                headers=headers,
                json={
                    'query': current_query,
                    'variables': variables
                }
            )
            
            if response.status_code != 200:
                raise Exception(f"Error en la API: {response.status_code} - {response.text}")
            
            data = response.json()
            
            if 'errors' in data:
                raise Exception(f"Error en GraphQL: {data['errors']}")
            
            objects_data = data['data'][objects]
            all_objects.extend(objects_data['edges'])
            
            # Verificar si hay más páginas
            page_info = objects_data['pageInfo']
            has_next_page = page_info['hasNextPage']
            cursor = page_info.get('endCursor')
        
        # Procesar y formatear los datos
        formatted_objects = []
        
        for edge in all_objects:
            object = edge['node']
            
            # Aplicar filtro de exclusión si se especifica
            if exclude and object['handle'] in exclude:
                continue
            
            # Formatear según el ejemplo proporcionado
            formatted_object = {
                "id": object['id'],
                "handle": object['handle'],
                "title": object['title'],
                "description": object['description'] or "",
                "url": f"https://{self.shop_url.replace('.myshopify.com', '')}.ca/{objects}/{object['handle']}",
                "seo": {
                    "title": object['seo']['title'] or "",
                    "description": object['seo']['description'] or ""
                },
                "product_count": object['productsCount']['count'],
                "semantic_keywords": self.generate_semantic_keywords(object['title'], object['description']),
                "priority": self.determine_priority(object['productsCount']['count']),
                "updated_at": object['updatedAt']
            }
            
            formatted_objects.append(formatted_object)
        
        return {
            objects: formatted_objects
        }

    def generate_semantic_keywords(self, title: str, description: str) -> List[str]:
        """
        Genera palabras clave semánticas basadas en el título y descripción.
        Esta es una implementación básica - puedes mejorarla según tus necesidades.
        """
        keywords = []
        
        # Extraer palabras clave del título
        title_words = title.lower().split()
        keywords.extend([word for word in title_words if len(word) > 3])
        
        # Extraer algunas palabras clave de la descripción
        if description:
            desc_words = description.lower().split()[:10]  # Primeras 10 palabras
            keywords.extend([word for word in desc_words if len(word) > 4])
        
        # Remover duplicados y limitar a 6 palabras clave
        unique_keywords = list(dict.fromkeys(keywords))[:6]
        
        return unique_keywords

    def determine_priority(self, product_count: int) -> str:
        """
        Determina la prioridad basada en el número de productos.
        """
        if product_count >= 100:
            return "high"
        elif product_count >= 50:
            return "medium"
        else:
            return "low"
    