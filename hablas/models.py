from django.db import models
from django.conf import settings


class Habla(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    likes  = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.text} - ({self.post_date}) - ({self.author.username})'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    post_date = models.DateTimeField()
    comment_text = models.CharField(max_length=255)
    Habla = models.ForeignKey(Habla, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.comment_text}" - ({self.post_date}) - ({self.author.username})'