from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="post/", null=True)
    #usuario
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    #categoria
    permitir_comentarios = models.BooleanField(default = True)

    def __str__(self):
        return self.titulo