from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "contenido", "imagen", "permitir_comentarios")

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'class' : 'validate','placeholder' : 'titulo del post', 'type' : 'text'})
        self.fields["contenido"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Escriba su post', 'type' : 'text'})
        self.fields["imagen"].widget.attrs.update({'class' : 'texto-rojo','placeholder' : 'ingrese su nombre', 'type' : 'file'})
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)