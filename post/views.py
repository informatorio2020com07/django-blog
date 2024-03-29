from django.shortcuts import render, redirect, HttpResponse
from .models import Post,Categoria,CalificacionPost
from .forms import PostForm,ComentarioForm,CategoriaForm, SearchForm
from django.contrib.auth.decorators import login_required


def index(request):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", "")
    orden_post = request.GET.get("orden", None)
    param_comentarios_habilitados = request.GET.get("permitir_comentarios", None)
    param_categorias = request.GET.getlist("categoria")


    posts = Post.objects.filter(titulo__icontains = filtro_titulo)
    
    if param_comentarios_habilitados:
        posts = posts.filter(permitir_comentarios = True)
    if param_categorias:
        posts = posts.filter(categoria__id__in = param_categorias)

    if orden_post == "titulo":
        posts= posts.order_by("titulo")
    elif orden_post == "antiguo":
        posts= posts.order_by("fecha_creado")
    elif orden_post == "nuevo":
        posts= posts.order_by("-fecha_creado")


    contexto = {"posts":posts,
                "search_form":search_form,
                }
    return render(request, "post/index.html",contexto)


def show_post(request,id):
    post=Post.objects.get(pk=id)

    usuario=post.usuario
    form_comentario=ComentarioForm()
    mas_post = Post.objects.filter(usuario_id=usuario)
    
    comentarios = post.comentario_set.all().order_by("-fecha_creacion")

    if request.user.is_authenticated:
        calif = request.user.detalle_calificacion.filter(post=post).first()
        if calif:
            calificacion = calif.calificacion
        else:
            calificacion = 0
    else:
        calificacion = 0

    contexto = {
    "mas_post":mas_post,
    "post":post,
    "form_comentario":form_comentario,
    "comentarios":comentarios,
    "calificacion":calificacion,
    }
    return render(request,"post/post.html",contexto)

#decorador que controla el login del usuario cambiar en settings destino
@login_required
def new_post(request):
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
    contexto = {
        "form":form,
        }
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
    else:
        return redirect("post", post.id)




@login_required
def borrar_post(request,id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        if post.usuario == request.user:
            post.delete()
            return redirect("ver_perfil", request.user.id)

@login_required
def calificar_post(request, id, calificacion):
    perfil = request.user
    post = Post.objects.get(pk=id)
    calif = perfil.detalle_calificacion.filter(post=post).first()

    if calif:
        calif.calificacion = calificacion
    else:
        calif = CalificacionPost()
        calif.post = post
        calif.calificacion = calificacion
        calif.usuario = perfil

    try:
        calif.full_clean() 
        calif.save()
    except Exception as ex: 
        return HttpResponse("error")
    return redirect("post", post.id)



def list_categoria(request):
    categorias = Categoria.objects.all()
    contexto = {
        "categorias":categorias,
    }
    return render(request, "post/categoria/categorias.html", contexto)

def show_categoria(request,id):
    cat=Categoria.objects.get(pk=id)
    posts = Post.objects.filter(categoria=cat)
    contexto = {
        "posts":posts,
        "categoria":cat,
    }
    return render(request, "post/categoria/show_categoria.html",contexto)

@login_required
def feed(request):
    seguidos = request.user.seguidos.all()
    posts = Post.objects.filter(usuario__in=seguidos.all())
    contexto = {
        "posts":posts,
        }
    return render(request, "post/index.html",contexto)