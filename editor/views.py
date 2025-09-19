from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, DetailView
from .forms import ContentPromptForm

class ContentPromptForm(FormView):
    template_name = 'editor/content_prompt_form.html'
    form_class = ContentPromptForm
    success_url = '/editor/settings.html'

class ContentCreateView(TemplateView):
    template_name = 'editor/content.html'

class ContentEditView(DetailView):
    template_name = 'editor/content.html'
