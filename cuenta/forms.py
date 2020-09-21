from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

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
        lista=["Nombre","Apellido","Usuario","Email","contraseña","repetir contraseña"]
        for x,valor in enumerate(self.fields):
            self.fields[valor].widget.attrs.update({'class' : 'validate','placeholder' : lista[x], 'type' : 'text'})
            if x==len(lista)-1:
                break
        self.fields["nacimiento"].widget.attrs.update({'class' : 'validate','placeholder' : "", 'type' : 'date'})
        self.fields["foto"].widget.attrs.update({'class' : 'texto-rojo','placeholder' : '', 'name':'foto' , 'accept':'image/*'})


class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username", "email", "password", "nacimiento", "foto")