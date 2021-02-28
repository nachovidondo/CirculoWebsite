from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import get_object_or_404, render
from . models import PostInicio, Category, PostImagenes
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    inicios= PostInicio.objects.filter(categories=Category.objects.get(nombre="Inicio"))
    return render (request,'App1/inicio.html',{'inicios' : inicios})


def articulos(request, postinicio_id):
    articulos = get_object_or_404(PostInicio, pk = postinicio_id)
    return render (request,'App1/articulos.html',{'articulos' : articulos})


