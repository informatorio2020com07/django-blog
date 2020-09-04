from django import forms
from .models import Post,Comentario,Categoria,Calificacion_post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "contenido", "imagen", "permitir_comentarios","categoria")
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'class' : 'validate','placeholder' : 'titulo del post', 'type' : 'text'})
        self.fields["contenido"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Escriba su post', 'type' : 'text'})
        self.fields["imagen"].widget.attrs.update({'class' : 'texto-rojo','placeholder' : '', 'type' : 'file'})
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})
        self.fields["categoria"].widget.attrs.update({'class' : '','placeholder' : '', 'type' : ''})        

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields =("texto",)
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields["texto"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Escriba su comentario', 'type' : 'text'})

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("titulo","descripcion")