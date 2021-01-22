from django.shortcuts import render
from .models import Category, Post
# Create your views here.


def ventas(request):
    return render (request,'Venta/ventas.html')
def venta_departamentos(request):
    return render(request,'Venta/venta_departamentos.html')
def venta_monoambientes(request):
    monoambientes= Post.objects.filter(categories=Category.objects.get(nombre="Monoambientes"))
    return render(request,'Venta/venta_monoambientes.html',{'monoambientes': monoambientes})
def venta_dptoundormi(request):
    dptoundormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 1 Dormitorio"))
    return render(request,'Venta/venta_dptoundormi.html',{'dptoundormis': dptoundormis})
def venta_dptodosdormi(request):
    dptodosdormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 2 Dormitorios"))
    return render(request,'Venta/venta_dptodosdormi.html',{'dptodosdormis': dptodosdormis})
def venta_dptotresdormi(request):
    dptotresdormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 3 Dormitorios"))
    return render(request,'Venta/venta_dptotresdormi.html',{'dptotresdormis': dptotresdormis})
def venta_casas(request):
    return render(request,'Venta/venta_casas.html')
def venta_casadosdormi(request):
    casadosdormis=Post.objects.filter(categories=Category.objects.get(nombre ="Casas 2 Dormitorios"))
    return render(request,'Venta/venta_casadosdormi.html',{'casadosdormis':casadosdormis})
def venta_casatresdormi(request):
    casatresdormis=Post.objects.filter(categories=Category.objects.get(nombre = "Casas 3 Dormitorios"))
    return render(request,'Venta/venta_casatresdormi.html',{ 'casatresdormis':casatresdormis})
def venta_casacuatrodormi(request):
    casacuatrodormis=Post.objects.filter(categories=Category.objects.get(nombre ="Casas 4 Dormitorios"))
    return render(request,'Venta/venta_casacuatrodormi.html',{ 'casacuatrodormis':casacuatrodormis})
def venta_casacincodormi(request):
    casacincodormis=Post.objects.filter(categories=Category.objects.get(nombre = "Casas 5 Dormitorios"))
    return render(request,'Venta/venta_casacincodormi.html',{ 'casacincodormis':casacincodormis})
def venta_locales(request):
    locales= Post.objects.filter(categories=Category.objects.get(nombre="Locales"))
    return render(request,'Venta/venta_locales.html',{'locales': locales})
def venta_oficinas(request):
    oficinas= Post.objects.filter(categories=Category.objects.get(nombre="Oficinas"))
    return render(request,'Venta/venta_oficinas.html',{'oficinas': oficinas})
def venta_terrenos(request):
    terrenos= Post.objects.filter(categories=Category.objects.get(nombre="Terrenos"))
    return render(request,'Venta/venta_terrenos.html',{'terrenos': terrenos})
def venta_duplex(request):
    return render(request,'Venta/venta_duplex.html')
def venta_duplexdosdormi(request):
    duplexdosdormis= Post.objects.filter(categories=Category.objects.get(nombre="Duplex 2 Dormitorios"))
    return render(request,'Venta/venta_duplexdosdormi.html',{'duplexdosdormis': duplexdosdormis})
def venta_duplextresdormi(request):
    duplextresdormis= Post.objects.filter(categories=Category.objects.get(nombre="Duplex 3 Dormitorios"))
    return render(request,'Venta/venta_duplextresdormi.html',{'duplextresdormis': duplextresdormis})