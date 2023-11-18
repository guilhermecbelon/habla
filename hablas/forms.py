from django.forms import ModelForm
from .models import *

class HablaForm(ModelForm):
    class Meta:
        model = Habla
        fields = [
            'author',
            'text',
            'cattegory'
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Habla',
            'cattegory': 'Categorias'
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'comment_text',
        ]
        labels = {
            'author': 'Usuário',
            'comment_text': 'Comentário',
        }