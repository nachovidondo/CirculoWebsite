from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Post


def ventas(request):
    return render (request,'Venta/ventas.html')
def venta_departamentos(request):
    return render(request,'Venta/venta_departamentos.html')

#Departamentos Paginados
def venta_monoambientes(request):
    venta_monoambientes= Post.objects.filter(categories=Category.objects.get(nombre="Monoambientes"))
    paginator = Paginator(venta_monoambientes, 3)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request,'Venta/venta_monoambientes.html',{'venta_monoambientes': page_articles})
def venta_dptoundormi(request):
    venta_dptoundormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 1 Dormitorio"))
    paginator = Paginator(venta_dptoundormis, 3)
    page = request.GET.get('page')
    page_articles_dptoundormi = paginator.get_page(page)
    return render(request,'Venta/venta_dptoundormi.html',{'venta_dptoundormis': page_articles_dptoundormi})
def venta_dptodosdormi(request):
    venta_dptodosdormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 2 Dormitorios"))
    paginator = Paginator(venta_dptodosdormis, 3)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request,'Venta/venta_dptodosdormi.html',{'venta_dptodosdormis': page_articles})


def venta_dptotresdormi(request):
    venta_dptotresdormis= Post.objects.filter(categories=Category.objects.get(nombre="Departamento 3 Dormitorios"))
    return render(request,'Venta/venta_dptotresdormi.html',{'venta_dptotresdormis': venta_dptotresdormis})
def venta_casas(request):
    return render(request,'Venta/venta_casas.html')
def venta_casadosdormi(request):
    venta_casadosdormis=Post.objects.filter(categories=Category.objects.get(nombre ="Casas 2 Dormitorios"))
    return render(request,'Venta/venta_casadosdormi.html',{'venta_casadosdormis':venta_casadosdormis})
def venta_casatresdormi(request):
    venta_casatresdormis=Post.objects.filter(categories=Category.objects.get(nombre = "Casas 3 Dormitorios"))
    return render(request,'Venta/venta_casatresdormi.html',{ 'venta_casatresdormis':venta_casatresdormis})
def venta_casacuatrodormi(request):
    venta_casacuatrodormis=Post.objects.filter(categories=Category.objects.get(nombre ="Casas 4 Dormitorios"))
    return render(request,'Venta/venta_casacuatrodormi.html',{ 'venta_casacuatrodormis':venta_casacuatrodormis})
def venta_casacincodormi(request):
    venta_casacincodormis=Post.objects.filter(categories=Category.objects.get(nombre = "Casas 5 Dormitorios"))
    return render(request,'Venta/venta_casacincodormi.html',{ 'venta_casacincodormis':venta_casacincodormis})
def venta_locales(request):
    venta_locales= Post.objects.filter(categories=Category.objects.get(nombre="Locales"))
    return render(request,'Venta/venta_locales.html',{'venta_locales': venta_locales})
def venta_oficinas(request):
    venta_oficinas= Post.objects.filter(categories=Category.objects.get(nombre="Oficinas"))
    return render(request,'Venta/venta_oficinas.html',{'venta_oficinas':venta_oficinas})
def venta_terrenos(request):
    venta_terrenos= Post.objects.filter(categories=Category.objects.get(nombre="Terrenos"))
    return render(request,'Venta/venta_terrenos.html',{'venta_terrenos': venta_terrenos})
def venta_duplex(request):
    return render(request,'Venta/venta_duplex.html')
def venta_duplexdosdormi(request):
    venta_duplexdosdormis= Post.objects.filter(categories=Category.objects.get(nombre="Duplex 2 Dormitorios"))
    return render(request,'Venta/venta_duplexdosdormi.html',{'venta_duplexdosdormis': venta_duplexdosdormis})
def venta_duplextresdormi(request):
    venta_duplextresdormis= Post.objects.filter(categories=Category.objects.get(nombre="Duplex 3 Dormitorios"))
    return render(request,'Venta/venta_duplextresdormi.html',{'venta_duplextresdormis': venta_duplextresdormis})
def venta_galpones(request):
    venta_galpones= Post.objects.filter(categories=Category.objects.get(nombre="Galpones"))
    return render(request,'Venta/venta_galpones.html',{'venta_galpones': venta_galpones})

#Detalles por cada articulo
def articulos_venta(request, post_id):
    articulos_venta = get_object_or_404(Post, pk = post_id)
    return render (request,'Venta/articulos_venta.html',{'articulos_venta' : articulos_venta})
def ofice_local_details_ventas(request, post_id):
    ofice_local_details_ventas = get_object_or_404(Post, pk = post_id)
    return render (request,'Venta/ofice_local_details_ventas.html',{'ofice_local_details_ventas' : ofice_local_details_ventas})
def monoambiente_details_ventas(request, post_id):
    monoambiente_details_ventas = get_object_or_404(Post, pk = post_id)
    return render (request,'Venta/monoambiente_details_ventas.html',{'monoambiente_details_ventas' : monoambiente_details_ventas})
def galpones_detail_ventas(request, post_id):
    galpones_detail_ventas = get_object_or_404(Post, pk = post_id)
    return render (request,'Venta/galpones_detail_ventas.html',{'galpones_detail_ventas' : galpones_detail_ventas})