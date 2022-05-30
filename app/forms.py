from django import forms
from .models import carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = carro
        fields = fields = ['modelo', 'marca', 'ano', 'valor', 'img']