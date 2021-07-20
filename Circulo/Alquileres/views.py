from . models import PostAlquiler
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Category, PostAlquiler




def alquileres(request):
    return render (request,'Alquileres/alquiler.html')
def alqui_departamentos(request):
    return render(request,'Alquileres/alqui_departamentos.html')
def alqui_monoambientes(request):
    monoambientes= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Monoambientes"))
    paginator = Paginator(monoambientes, 3)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request,'Alquileres/alqui_monoambientes.html',{'monoambientes': page_articles})
        
def alqui_dptoundormi(request):
    dptoundormis= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Departamento 1 Dormitorio"))
    paginator = Paginator(dptoundormis, 3)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request,'Alquileres/alqui_dptoundormi.html',{'dptoundormis': page_articles})
def alqui_dptodosdormi(request):
    dptodosdormis= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Departamento 2 Dormitorios"))
    paginator = Paginator(dptodosdormis, 3)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request,'Alquileres/alqui_dptodosdormi.html',{'dptodosdormis': page_articles})
def alqui_dptotresdormi(request):
    dptotresdormis= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Departamento 3 Dormitorios"))
    return render(request,'Alquileres/alqui_dptotresdormi.html',{'dptotresdormis': dptotresdormis})
def alqui_casas(request):
    return render(request,'Alquileres/alqui_casas.html')
def alqui_casadosdormi(request):
    casadosdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre ="Casas 2 Dormitorios"))
    return render(request,'Alquileres/alqui_casadosdormi.html',{'casadosdormis':casadosdormis})
def alqui_casatresdormi(request):
    casatresdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 3 Dormitorios"))
    return render(request,'Alquileres/alqui_casatresdormi.html',{ 'casatresdormis':casatresdormis})
def alqui_casacuatrodormi(request):
    casacuatrodormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre ="Casas 4 Dormitorios"))
    return render(request,'Alquileres/alqui_casacuatrodormi.html',{ 'casacuatrodormis':casacuatrodormis})
def alqui_casacincodormi(request):
    casacincodormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 5 Dormitorios"))
    return render(request,'Alquileres/alqui_casacincodormi.html',{ 'casacincodormis':casacincodormis})
def alqui_locales(request):
    locales= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Locales"))
    return render(request,'Alquileres/alqui_locales.html',{'locales': locales})
def alqui_oficinas(request):
    oficinas= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Oficinas"))
    return render(request,'Alquileres/alqui_oficinas.html',{'oficinas': oficinas})
def alqui_terrenos(request):
    terrenos= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Terrenos"))
    return render(request,'Alquileres/alqui_terrenos.html',{'terrenos': terrenos})
def alqui_duplex(request):
    return render(request,'Alquileres/alqui_duplex.html')
def alqui_duplexdosdormi(request):
    duplexdosdormis= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Duplex 2 Dormitorios"))
    return render(request,'Alquileres/alqui_duplexdosdormi.html',{'duplexdosdormis': duplexdosdormis})
def alqui_duplextresdormi(request):
    duplextresdormis= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Duplex 3 Dormitorios"))
    return render(request,'Alquileres/alqui_duplextresdormi.html',{'duplextresdormis': duplextresdormis})
def alqui_galpones(request):
    alqui_galpones= PostAlquiler.objects.filter(categories=Category.objects.get(nombre="Galpones"))
    return render(request,'Alquileres/alqui_galpones.html',{'alqui_galpones': alqui_galpones})

def article(request, postalquiler_id):
    articles = get_object_or_404(PostAlquiler, pk = postalquiler_id)
    return render (request,'Alquileres/article.html',{'articles' : articles})
def ofice_local_details_alquis(request, postalquiler_id):
    ofice_local_details_alquis = get_object_or_404(PostAlquiler, pk = postalquiler_id)
    return render (request,'Alquileres/ofice_local_details_alquis.html',{'ofice_local_details_alquis' : ofice_local_details_alquis})
def monoambiente_details_alquis(request, postalquiler_id):
    monoambiente_details_alquis = get_object_or_404(PostAlquiler, pk = postalquiler_id)
    return render (request,'Alquileres/monoambiente_details_alquis.html',{'monoambiente_details_alquis' : monoambiente_details_alquis})
def galpones_detail_alqui(request, postalquiler_id):
    galpones_detail_alqui = get_object_or_404(PostAlquiler, pk = postalquiler_id)
    return render (request,'Alquileres/galpones_detail_alqui.html',{'galpones_detail_alqui' : galpones_detail_alqui})


    