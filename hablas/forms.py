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