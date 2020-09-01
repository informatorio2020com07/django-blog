from django.shortcuts import render,redirect
#cerrar sesion
from django.contrib.auth import logout
#iniciar sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
#crear usuario
from django.contrib.auth.forms import UserCreationForm

def bienvenido(request):
    return render(request,"cuenta/bienvenido.html", {})

def bienvenido_premium(request):
    if request.user.is_authenticated:
        return render(request, "cuenta/bienvenido_premium.html", {})
    else:
        return redirect("iniciar_sesion")

def nuevo_usuario(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request,user)
                return redirect("bienvenido")
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
                return redirect("bienvenido")
    return render(request, "cuenta/login.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("bienvenido")