from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import get_object_or_404, render
from . models import PostInicio, Category, PostImagenes

# Create your views here.
def inicio(request):
    inicios = PostInicio.objects.filter(categories = Category.objects.get(nombre ="Inicio"))
    return render(request, 'App1/inicio.html', {'inicios': inicios})

def articulo(request, postinicio_id):
    articulos = get_object_or_404(PostInicio, pk = postinicio_id)
    return render (request,'App1/articulo.html',{'articulos':articulos})

def tasaciones(request):
    return render(request, 'App1/tasaciones.html')

