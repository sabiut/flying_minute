from django import forms
from.models import BoardPaper


class DocumentForm(forms.ModelForm):
    class Meta:
        model = BoardPaper
        fields = ('description', 'document', )