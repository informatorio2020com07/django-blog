from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.urls import reverse
from cuenta.models import Perfil

class TestPrueba(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_placeholder(self):
        self.browser.get(self.live_server_url)
        search_field = self.browser.find_element_by_id("id_titulo")
        placeholder = search_field.get_property("placeholder")
        self.assertEqual(placeholder, "titulo")

    def test_barra_busqueda(self):
        self.browser.get(self.live_server_url)
        search_field = self.browser.find_element_by_id("id_titulo")
        search_field.send_keys("django docs")
        search_field.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        search_field = self.browser.find_element_by_id("id_titulo")
        texto = search_field.get_property("value")
        self.assertEquals(texto, "django docs")

    def test_crear_post_sin_login(self):
        self.browser.get(self.live_server_url)
        #/html/body/header/nav/div/div/div[1]/div/div[4]/a
        nuevo_post = self.browser.find_element_by_xpath('/html/body/header/nav/div/div/div[1]/div/div[4]/a')
        nuevo_post.click()
        self.browser.implicitly_wait(5)
        url_actual = self.browser.current_url
        url_login = self.live_server_url + reverse("iniciar_sesion") + "?next=/post/new"
        print("actual: ", url_actual)
        print("url login: ", url_login)
        self.assertEquals(url_actual, url_login)


    def test_crear_post_con_login(self):
        usuario = Perfil()
        usuario.username = "sandra"
        usuario.set_password("Clave#1234")
        usuario.save()

        self.browser.get(self.live_server_url)
        #/html/body/header/nav/div/div/div[1]/div/div[4]/a
        nuevo_post = self.browser.find_element_by_xpath('/html/body/header/nav/div/div/div[1]/div/div[4]/a')
        nuevo_post.click()
        self.browser.implicitly_wait(5)

        username_input = self.browser.find_element_by_id("id_username")
        password_input = self.browser.find_element_by_id("id_password")
        username_input.send_keys(usuario.username)
        password_input.send_keys("Clave#1234")

        password_input.send_keys(Keys.ENTER)

        url_actual = self.browser.current_url
        url_crear_post = self.live_server_url + reverse("new_post")
        self.assertEquals(url_actual, url_crear_post)