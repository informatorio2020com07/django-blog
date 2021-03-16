from django.urls import path
from . import views

from django.contrib.auth import views as auth_view

urlpatterns = [
    path("bienvenido", views.bienvenido, name="bienvenido"),
    path("bienvenido_premium", views.bienvenido_premium, name="bienvenido_premium"),
    path("nuevo", views.nuevo_usuario, name="nuevo_usuario"),
    path("login", views.iniciar_sesion, name="iniciar_sesion"),
    path("logout", views.cerrar_sesion, name="cerrar_sesion"),
    path("perfil/<int:id>", views.ver_perfil, name="ver_perfil"),
    path("perfil/<int:id>/seguir", views.seguir_perfil, name="seguir_perfil"),

    path("perfil/editar", views.editar_perfil, name="editar_perfil"),
    path("perfil/cambiar_clave", views.editar_password, name="editar_password"),

    #resetear password
    path("perfil/reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path("perfil/confirmar/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("perfil/por/<uidb64>/<token>", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("perfil/reset_completo/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("enviar_correo/", views.enviar_correo, name="enviar_correo"),


]
