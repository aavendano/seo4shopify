
from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.ContentPromptForm.as_view(), name='content_prompt'),
    #path('content/create', views.ContentCreateView.as_view(), name='content_create'),
    #path('content/edit/<int:pk>', views.ContentEditView.as_view(), name='content_edit')
]