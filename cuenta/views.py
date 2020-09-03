from django.shortcuts import render,redirect
#cerrar sesion
from django.contrib.auth import logout
#iniciar sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
#crear usuario
from .forms import NuevoUsuarioForm
#fin crear usuario
from .models import Perfil

def bienvenido(request):
    return render(request,"cuenta/bienvenido.html", {})

def bienvenido_premium(request):
    if request.user.is_authenticated:
        return render(request, "cuenta/bienvenido_premium.html", {})
    else:
        return redirect("iniciar_sesion")

def nuevo_usuario(request):
    form = NuevoUsuarioForm()
    if request.method == "POST":
        form = NuevoUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request,user)
                return redirect("index")
    return render(request, "cuenta/nuevo_usuario.html",{"form":form})

def iniciar_sesion(request):
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
    return render(request, "cuenta/login.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("index")

def ver_perfil(request,id):
    perfil = Perfil.objects.get(pk=id)
    contexto = {
        "perfil":perfil,
        }
    template = "cuenta/perfil.html"
    return render(request, template, contexto)    