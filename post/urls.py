from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("post/<int:id>", views.show_post, name="post"),
path("post/new", views.new_post,name="new_post"),
path("post/<int:id>/comentar", views.comentar, name="comentar"),
path("post/categoria/<int:id>", views.show_categoria,name="show_categoria"),
path("post/<int:id>/like", views.like, name="like"),
path("post/<int:id>/borrar", views.borrar_post, name="borrar_post"),
path("prueba/<int:valor>/<int:otrovalor>/", views.probando, name="prueba")
]
