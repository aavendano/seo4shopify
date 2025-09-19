from django import forms
from tinymce.widgets import TinyMCE

class ContentPromptForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=255)
    tone = forms.ChoiceField(choices=[('formal', 'Formal'), ('informal', 'Informal')], label='Tone')    
    words = forms.IntegerField(label='Length', min_value=1, max_value=10)
    main_keyword = forms.CharField(label='Main Keyword', max_length=255)
    additional_keywords = forms.CharField(label='Additional Keywords (comma-separated)', max_length=255, required=False)



class ContentCanvasForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    content = forms.CharField(label='Content', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))