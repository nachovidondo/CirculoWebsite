from django.shortcuts import render
from . models import Inicio
# Create your views here.
def inicio(request):
    inicio1 = Inicio.objects.get(id=1)
    inicio2 = Inicio.objects.get(id=2)
    inicio3 = Inicio.objects.get(id=3)
    
    inicios= [inicio1, inicio2 ,inicio3]


    return render(request, 'App1/inicio.html',{'inicios' : inicios})


def tasaciones(request):
    
    return render(request,'App1/tasaciones.html')