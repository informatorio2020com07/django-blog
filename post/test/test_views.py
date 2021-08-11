from django.test import TestCase, Client
from django.urls import reverse
from post.models import Post, Comentario, Categoria
from cuenta.models import Perfil


class TestViews(TestCase):

    def setUp(self):
        self.cliente = Client()
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

    def test_index_get(self):
        response = self.cliente.get(reverse("index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "post/index.html")

    def test_comentar(self):
        self.cliente.force_login(self.perfil1)
        response = self.cliente.post(reverse("comentar", args=[self.post1.id]),
        {
            "texto": "comentario post1"
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Comentario.objects.all().count(),1)
        self.assertEquals(Comentario.objects.last().texto,"comentario post1")

    def test_comentar_datos_no_validos(self):
        self.cliente.force_login(self.perfil1)
        response = self.cliente.post(reverse("comentar", args=[self.post1.id]))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Comentario.objects.all().count(),0)