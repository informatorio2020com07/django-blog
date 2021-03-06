from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
path("", views.index, name="index"),
path("post/<int:id>/", views.show_post, name="post"),
path("post/new", views.new_post,name="new_post"),
path("post/<int:id>/comentar", views.comentar, name="comentar"),
path("post/<int:id>/borrar", views.borrar_post, name="borrar_post"),
path("post/<int:id>/calificar/<int:calificacion>/", views.calificar_post, name="calificar_post"),

path("categoria/", views.list_categoria,name="categorias"),
path("categoria/<int:id>/", views.show_categoria,name="categoria"),
path("mi_feed/", views.feed, name="feed")
]
