from django.forms import ModelForm
from .models import *

class HablaForm(ModelForm):
    class Meta:
        model = Habla
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Habla',
        }