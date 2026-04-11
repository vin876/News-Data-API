from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    link = models.URLField(unique=True)
    fonte = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
