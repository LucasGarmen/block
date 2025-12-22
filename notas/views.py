from django.urls import path
from . import views
from django.http import response
from django.shortcuts import render, redirect,get_object_or_404
from .models import Notas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm


from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')

        Notas.objects.create(
            usuario=request.user,   # 👈 guardamos el usuario actual
            titulo=titulo,
            contenido=contenido
        )

    notas = Notas.objects.filter(usuario = request.user)
    return render(request, 'notas/index.html', {'notas': notas})


def editar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    if request.method == 'POST':
        nota.titulo = request.POST.get('titulo')
        nota.contenido = request.POST.get('contenido')
        nota.save()
        return redirect('inicio')
    return render(request,'notas/editar.html',{'nota':nota})

def eliminar_nota(request, id):
    if request.method == 'POST':
        nota = get_object_or_404(Notas, id=id)
        nota.delete()
    return redirect('inicio')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html',{'form':form})



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})
