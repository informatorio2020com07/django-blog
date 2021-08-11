from django.test import TestCase
from post.models import Post, Categoria
from cuenta.models import Perfil

class TestModels(TestCase):

    def setUp(self):
        self.cat1 = Categoria.objects.create(
            titulo="cat1",
            descripcion="desc1"
        )
        self.perfil1 = Perfil.objects.create(
            username="axel"
        )
        self.post1 = Post.objects.create(
            titulo="post1",
            contenido="post1 contenido",
            permitir_comentarios = True,
            categoria = self.cat1,
            usuario = self.perfil1
        )

    def test_post_estado_defecto(self):
        self.assertEquals(self.post1.estado, Post.ESTADO_PUBLICO)
    
    def test_titulo_mas_categoria(self):
        self.assertEquals(self.post1.titulo_mas_categoria(), "post1-cat1")