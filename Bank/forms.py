from django import forms
from .models import detail

class DetailForm(forms.ModelForm):
    ifsc=forms.CharField()

    class Meta:
        model = detail
        fields = ['ifsc']
