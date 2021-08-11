from django.test import SimpleTestCase
from post.forms import ComentarioForm

class TestForm(SimpleTestCase):
    def test_comentario_form_valido(self):
        form = ComentarioForm(data={
            "texto":"textp del comentario"
        })

        self.assertTrue(form.is_valid())

    def test_comentario_form_no_valido(self):
        form = ComentarioForm()
        self.assertFalse(form.is_valid())