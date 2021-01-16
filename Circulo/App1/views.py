from django.shortcuts import render
from . models import Inicio
# Create your views here.
def inicio(request):
  
    inicios= Inicio.objects.all()


    return render(request, 'App1/inicio.html',{'inicios' : inicios})


def tasaciones(request):
    
    return render(request,'App1/tasaciones.html')
def acercanuestro(request):
    return render (request,'App1/aboutus.html')