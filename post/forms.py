from django import forms
from .models import Post,Comentario,Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "contenido", "imagen", "permitir_comentarios","categoria")
    #def __init__(self,variables_extras, *args, **kwargs):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'class' : 'validate','placeholder' : 'titulo del post', 'type' : 'text'})
        self.fields["contenido"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Escriba su post', 'type' : 'text'})
        self.fields["imagen"].widget.attrs.update({'class' : 'texto-rojo','placeholder' : '', 'type' : 'file'})
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})
        self.fields["categoria"].widget.attrs.update({'class' : '','placeholder' : '', 'type' : ''})

        #self.fields["categoria"].queryset = Categoria.objects.filter(titulo__icontains = "" )

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

class SearchForm(forms.Form):
    titulo = forms.CharField(max_length=30, required = False)
    ORDER_OPCIONES = (
        ("titulo", "Titulo"),
        ("Fecha",(
            ("antiguo", "Antiguo"),
            ("nuevo", "Nuevo"))
        ))
    orden = forms.ChoiceField(choices=ORDER_OPCIONES, required = False,
        initial="nuevo")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple, required = False)
    permitir_comentarios = forms.BooleanField(required = False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs["placeholder"] = "titulo"
        self.fields["permitir_comentarios"].widget.attrs["class"] ="with-gap"