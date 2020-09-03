from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
#agrega mail
class NuevoUsuarioForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username", "email", "password1",
         "password2", "nacimiento", "foto")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)