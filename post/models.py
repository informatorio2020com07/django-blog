from django.db import models
from cuenta.models import Perfil

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="post/", null=True)
    usuario = models.ForeignKey(Perfil, on_delete = models.CASCADE,default=None )
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)
    permitir_comentarios = models.BooleanField(default = True)
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post=models.ForeignKey(Post, on_delete = models.CASCADE)
    usuario=models.ForeignKey(Perfil, on_delete = models.SET_NULL, null=True)
    texto = models.TextField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Calificacion_post(models.Model):
    post=models.ForeignKey(Post, on_delete = models.CASCADE)
    observador=models.ForeignKey(Perfil, on_delete = models.CASCADE)
    calificacion=models.IntegerField()

class Calificacion_comentario(models.Model):
    comentario=models.ForeignKey(Comentario, on_delete = models.CASCADE)
    observador=models.ForeignKey(Perfil, on_delete = models.CASCADE)
    calificacion=models.IntegerField() 

