from django.shortcuts import render
from .models import Category, Post
# Create your views here.

def ventas(request):
    casas= Post.objects.filter(categories=Category.objects.get(nombre="Casas"))
    return render(request,'Venta/ventas.html',{'casas': casas})



def venta_monoambientes(request):
    monoambientes= Post.objects.filter(categories=Category.objects.get(nombre="Monoambientes"))
    return render(request,'Venta/venta_monoambientes.html',{'monoambientes': monoambientes})
def venta_departamentos(request):
    return render(request,'Venta/venta_departamentos.html')
def venta_dptoundormi(request):
    dptoundormis= Post.objects.filter(categories=Category.objects.get(nombre="1 Dormitorio"))
    return render(request,'Venta/venta_dptoundormi.html',{'dptoundormis': dptoundormis})
def venta_dptodosdormi(request):
    dptodosdormis= Post.objects.filter(categories=Category.objects.get(nombre="2 Dormitorios"))
    return render(request,'Venta/venta_dptodosdormi.html',{'dptodosdormis': dptodosdormis})
def venta_dptotresdormi(request):
    dptotresdormis= Post.objects.filter(categories=Category.objects.get(nombre="3 Dormitorios"))
    return render(request,'Venta/venta_dptotresdormi.html',{'dptotresdormis': dptotresdormis})
def venta_casas(request):
    casas= Post.objects.filter(categories=Category.objects.get(nombre="Casas"))
    return render(request,'Venta/venta_casas.html',{'casas': casas})
    
def venta_locales(request):
    locales= Post.objects.filter(categories=Category.objects.get(nombre="Locales"))
    return render(request,'Venta/venta_locales.html',{'locales': locales})
def venta_oficinas(request):
    oficinas= Post.objects.filter(categories=Category.objects.get(nombre="Oficinas"))
    return render(request,'Venta/venta_oficinas.html',{'oficinas': oficinas})
def venta_terrenos(request):
    terrenos= Post.objects.filter(categories=Category.objects.get(nombre="Terrenos"))
    return render(request,'Venta/venta_terrenos.html',{'terrenos': terrenos})