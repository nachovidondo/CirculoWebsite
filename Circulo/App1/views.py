from django.shortcuts import render
from . models import PostInicio, Category, PostImagenes
# Create your views here.
def inicio(request):
    inicios= PostInicio.objects.filter(categories=Category.objects.get(nombre ="Inicio"))
    return render(request, 'App1/inicio.html',{'inicios' : inicios})


def tasaciones(request):
    
    return render(request,'App1/tasaciones.html')
def acercanuestro(request):
    return render (request,'App1/aboutus.html')