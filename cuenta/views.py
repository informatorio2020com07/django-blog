from django.shortcuts import render,redirect, HttpResponse
#cerrar sesion
from django.contrib.auth import logout
#iniciar sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
#crear usuario
from .forms import NuevoUsuarioForm
#fin crear usuario
from .models import Perfil
from post.models import Categoria
from django.contrib.auth.decorators import login_required

def bienvenido(request):
    categorias = Categoria.objects.all()
    return render(request,"cuenta/bienvenido.html", {"categorias":categorias,})

def bienvenido_premium(request):
    categorias = Categoria.objects.all()
    if request.user.is_authenticated:
        return render(request, "cuenta/bienvenido_premium.html", {"categorias":categorias,})
    else:
        return redirect("iniciar_sesion")

def nuevo_usuario(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        categorias = Categoria.objects.all()
        form = NuevoUsuarioForm()
        if request.method == "POST":
            form = NuevoUsuarioForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request,user)
                    return redirect("index")
        return render(request, "cuenta/nuevo_usuario.html",{"form":form,"categorias":categorias,})

def iniciar_sesion(request):
    categorias = Categoria.objects.all()
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
    return render(request, "cuenta/login.html", {"form":form,"categorias":categorias,})

def cerrar_sesion(request):
    logout(request)
    return redirect("index")

def ver_perfil(request,id):
    categorias = Categoria.objects.all()
    perfil = Perfil.objects.get(pk=id)
    seguido = False
    if request.user.is_authenticated:
        if request.user.seguidos.filter(id=perfil.id):
            seguido=True
    contexto = {
        "perfil":perfil,
        "categorias":categorias,
        "siguiendo":seguido
        }
    template = "cuenta/perfil.html"
    return render(request, template, contexto)

@login_required
def seguir_perfil(request, id):
    perfil_a_seguir = Perfil.objects.get(pk=id)
    perfil_seguidor = request.user
    if perfil_a_seguir != perfil_seguidor:
        if perfil_seguidor.seguidos.filter(id=perfil_a_seguir.id):
            perfil_seguidor.seguidos.remove(perfil_a_seguir)
        else:
            perfil_seguidor.seguidos.add(perfil_a_seguir)
        


    return redirect("ver_perfil", perfil_a_seguir.id)

@login_required
def editar_perfil(request, id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user:
        pass
    else:
        pass
    return HttpResponse("editar")
