from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="post/", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    #categoria
    permitir_comentarios = models.BooleanField(default = True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post=models.ForeignKey(Post, on_delete = models.CASCADE)
    usuario=models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    texto = models.TextField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)