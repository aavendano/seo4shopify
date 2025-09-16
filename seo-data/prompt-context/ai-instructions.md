# AI Instructions for SEO Internal Linking

## Primary Objective
Analyze blog articles and create optimized internal linking strategies that enhance user experience while improving SEO performance for PlayLoveToys.ca.

## Input Requirements

### 1. Article Content
- **Format**: HTML code of the blog article
- **Source**: Blog post HTML with existing structure and content
- **Requirements**: Complete article with headings, paragraphs, and existing formatting

### 2. Store Database
- **Collections data**: Complete list with handles, titles, descriptions, and URLs
- **Products data**: Product catalog with handles, titles, brands, and canonical URLs  
- **Blog articles**: Related content for cross-linking opportunities
- **Reserved keywords**: Mandatory linking rules and specific URLs

### 3. Configuration Files
- **SEO context**: Strategy guidelines and linking rules
- **Synonyms mapping**: Term variations and semantic relationships
- **Intent mapping**: User journey and funnel stage indicators
- **Anchor templates**: Natural language patterns for link text

## Analysis Process

### 1. Content Understanding
- Parse HTML structure and identify content sections
- Extract main topics, subtopics, and key themes
- Map user intent at different article sections
- Identify buyer journey stages (awareness → consideration → decision)

### 2. Link Opportunity Identification
- Scan for exact product mentions (mandatory linking)
- Find collection-relevant discussions and categories
- Identify educational content cross-linking opportunities
- Check for reserved keyword usage and apply mandatory rules

### 3. Link Selection and Optimization
- Apply semantic relevance criteria
- Ensure user value and expectation fulfillment
- Optimize for SEO benefit without over-optimization
- Create natural anchor text integration

### 4. Quality Assurance
- Verify link relevance and contextual value
- Ensure natural anchor text flow
- Confirm no self-linking to current collection
- Validate maximum 2 links per destination rule

## Output Requirements

### 1. Modified HTML Article

<article> <h1>Original Article Title</h1> <p>Content with integrated <a href="https://playlovetoys.ca/collections/example">natural anchor text</a> links...</p> </article>


### 2. Implementation Report

json { "article_analysis": {

"title": "Article Title",
"word_count": 1500,
"main_topics": ["topic1", "topic2"],
"user_intent_stages": ["awareness", "consideration"]
  
}, "linking_strategy": {

"total_links_added": 6,
"link_distribution": {
  "products": 2,
  "collections": 3,
  "articles": 1
}
  
}, "implemented_links": [

{
  "anchor_text": "sex toys for men collection",
  "target_url": "https://playlovetoys.ca/collections/sex-toys-for-men",
  "target_type": "collection",
  "placement_context": "paragraph discussing male pleasure products",
  "user_intent": "consideration",
  "seo_justification": "Targets high-value commercial keyword with strong semantic relevance",
  "user_value": "Directs users to relevant product category for purchase consideration"
},
{
  "anchor_text": "Tenga masturbators",
  "target_url": "https://playlovetoys.ca/collections/tenga",
  "target_type": "reserved_keyword",
  "placement_context": "section about Japanese innovation in adult toys",
  "user_intent": "decision",
  "seo_justification": "Mandatory reserved keyword link with brand-specific targeting",
  "user_value": "Provides direct access to specific brand products mentioned"
}
  
], "quality_metrics": {

"natural_integration_score": "95%",
"semantic_relevance_score": "92%",
"user_value_score": "88%"
  
}, "recommendations": [

"Consider adding related article links in future updates",
"Monitor click-through rates for anchor text optimization"
  
] }


## Technical Specifications
- **HTML preservation**: Maintain all original formatting, classes, and IDs
- **Link attributes**: Use standard `<a href="">` tags without additional attributes
- **URL format**: Always use canonical URLs with handles (not numeric IDs)
- **Encoding**: Preserve original HTML encoding and special characters


