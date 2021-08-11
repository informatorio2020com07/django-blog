from django.test import SimpleTestCase
from django.urls import reverse, resolve
from post import views

class TestUrls(SimpleTestCase):
    
    def test_url_index_resolved(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, views.index)

    def test_url_ver_post(self):
        #path("post/<int:id>", views.show_post, name="post"),
        url = reverse("post", args=[1])
        self.assertEquals(resolve(url).func, views.show_post)
        #vista basada en clases
        #self.assertEquals(resolve(url).func.view_class, views.show_post)