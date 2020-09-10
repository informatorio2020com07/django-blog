from django.db import models
from cuenta.models import Perfil
from .validators import validate_valor_calificacion
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.EmailField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="post/", null=True)
    usuario = models.ForeignKey(Perfil, on_delete = models.CASCADE,default=None, related_name="post_creados")
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)
    permitir_comentarios = models.BooleanField(default = True)

    lista_estados = (
        ("public", "Publico"),
        ("hidden", "Oculto")
        )
    estado = CharField(max_length=1,Choices=lista_estados)
    
    puntuadores = models.ManyToManyField(Perfil, blank=True, through="CalificacionPost", related_name="post_calificados")

    def __str__(self):
        return self.titulo

    def puntaje(self):
        puntaje = 0
        for x in self.calificacion_post_set.all():
            puntaje += x.calificacion
        return puntaje

    class Meta:
        verbose_name = "post_singular"
        verbose_name_plural = "post_plural"
        ordering = ("-fecha_creado",)

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

class CalificacionPost(models.Model):
    post=models.ForeignKey(Post, on_delete = models.CASCADE, related_name="calificacion")
    usuario=models.ForeignKey(Perfil, on_delete = models.CASCADE, related_name="detalle_calificacion")
    #calificacion=models.IntegerField(validators = [validate_valor_calificacion])
    calificacion=models.IntegerField(validators = [MaxValueValidator(5), MinValueValidator(-5)])

    class Meta: 
        unique_together = ("post","usuario")