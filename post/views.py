from django.shortcuts import render, redirect
from .models import Post,Categoria,Calificacion_post
from .forms import PostForm,ComentarioForm,CategoriaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()[0:12]
    categorias = Categoria.objects.all()
    contexto = {"posts":posts,
                "categorias":categorias,
                }
    return render(request, "post/index.html",contexto)


def show_post(request,id):

    post=Post.objects.get(pk=id)

    usuario=post.usuario
    categorias = Categoria.objects.all()
    form_comentario=ComentarioForm()
    mas_post = Post.objects.filter(usuario_id=usuario)
    #linea agregada
    comentarios = post.comentario_set.all().order_by("-fecha_creacion")
    contexto = {
    "mas_post":mas_post,
    "post":post,
    "form_comentario":form_comentario,
    "categorias":categorias,
    "comentarios":comentarios,
    }
    return render(request,"post/post.html",contexto)

#decorador que controla el login del usuario cambiar en settings destino
@login_required
def new_post(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        form= PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect("post", post.id)
        else:
            contexto={"form":form,
            "categorias":categorias,}
            return render(request, "post/new.html",contexto)
    form = PostForm()
    contexto={"form":form,
    "categorias":categorias,}
    return render(request, "post/new.html",contexto)

@login_required
def comentar(request,id):
    post=Post.objects.get(pk=id)
    if post.permitir_comentarios:
        if request.method == "POST":
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user
                comentario.post = post
                comentario.save()
                return redirect("post", post.id)
    else:
        return redirect("post", post.id)

def show_categoria(request,id):
    categorias = Categoria.objects.all()
    cat=Categoria.objects.get(pk=id)
    posts = Post.objects.filter(categoria=cat)
    contexto = {"posts":posts,
    "categorias":categorias,}
    return render(request, "post/index.html",contexto)

@login_required
def like(request,id):
    post=Post.objects.get(pk=id)
    print(post.id)
    print(request.user.id)
    cali=Calificacion_post.objects.filter(post=post)
    flag=True
    for x in cali:
        if x.observador==request.user:
            flag=False
    if flag:
        califi = Calificacion_post()
        califi.post=post
        califi.calificacion=1
        califi.observador=request.user
        califi.save()
    return redirect("post", post.id)


@login_required
def borrar_post(request,id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        if post.usuario == request.user:
            post.delete()
            return redirect("ver_perfil", request.user.id)