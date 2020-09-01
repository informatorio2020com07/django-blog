from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:id>", views.show_post, name="post"),
    path("post/new", views.new_post, name="new_post"),
]
