from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 20}),
        }
        