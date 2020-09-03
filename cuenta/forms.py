from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#agrega mail
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")

    #agrega control de mail a save
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    # me ayudo a darle forma pero me elimino el helptxt
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        lista=["Nombre","Apellido","Usuario","Email","contraseña","repetir contraseña"]
        for x,valor in enumerate(self.fields):
            self.fields[valor].widget.attrs.update({'class' : 'validate','placeholder' : lista[x], 'type' : 'text'})