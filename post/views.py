from django.shortcuts import render, redirect
from post.models import Post

from post.forms import PostForm, ComentarioForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()[0:12]
    template = "post/index.html"
    contexto = {"posts":posts}
    return render(request, template, contexto)

def show_post(request,id):
    post = Post.objects.get(pk=id)
    usuario = post.usuario
    lista_mas_post = Post.objects.filter(usuario_id=usuario.id)
    form_comentario = ComentarioForm()
    comentarios = post.comentario_set.all().order_by("-fecha_creacion")
    contexto = {
        "post":post,
        "mas_post":lista_mas_post,
        "form_comentario":form_comentario,
        "comentarios":comentarios,
        }
    template = "post/post.html"
    return render(request, template, contexto)

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect("post", post.id)
        else:
            template = "post/new.html"
            contexto = {"form":form}  
            return render(request,template,contexto)            
    
    form = PostForm()
    
    template = "post/new.html"
    contexto = {"form":form}
    
    return render(request,template,contexto)

@login_required
def comentar(request,id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.post = post
            comentario.save()
            return redirect("post", post.id)