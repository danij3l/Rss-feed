from django import forms
from .models import Rssf


class RssfForm(forms.ModelForm):
    class Meta:
    	model = Rssf
    	fields = ('title', 'url')
