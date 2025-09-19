from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import JsonResponse



class ChatView(TemplateView):
    template_name = 'chat/chat.html'
