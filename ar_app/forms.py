# ar_app/forms.py
from django import forms
from .models import ARModel

class UploadARModelForm(forms.ModelForm):
    class Meta:
        model = ARModel
        fields = ['name', 'glb_file']
