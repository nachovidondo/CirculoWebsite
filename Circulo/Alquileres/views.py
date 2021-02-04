from django.shortcuts import render,get_object_or_404
from . models import PostAlquiler, Category, PostImagenes

# Create your views here.
def alquiler(request):
    alquiler = PostAlquiler.objects.all()
    return render (request,'Alquileres/alquiler.html',{'alquiler':alquiler})
    

def alqui_monoambientes(request):
    monoambientes=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Monoambientes"))
    
    return render (request, 'Alquileres/alqui_monoambientes.html',{ 'monoambientes' : monoambientes })

def alqui_departamentos(request):
    return render(request,'Alquileres/alqui_departamentos.html')

def alqui_dptoundormi(request):
    dptoundormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Departamento 1 Dormitorio"))
    return render (request, 'Alquileres/alqui_dptoundormi.html',{ 'dptoundormis' : dptoundormis })

def alqui_dptodosdormi(request):
    dptodosdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Departamento 2 Dormitorios"))
    return render(request,'Alquileres/alqui_dptodosdormi.html',{ 'dptodosdormis':dptodosdormis})

def alqui_dptotresdormi(request):
    dptotresdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Departamento 3 Dormitorios"))
    return render(request,'Alquileres/alqui_dptotresdormi.html',{ 'dptotresdormis':dptotresdormis})

def alqui_casas(request):
    casas=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas"))
    return render(request,'Alquileres/alqui_casas.html',{ 'casas':casas})

def alqui_locales(request):
    locales=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Locales"))
    return render(request,'Alquileres/alqui_locales.html',{ 'locales':locales})

def alqui_oficinas(request):
    oficinas=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Oficinas"))
    return render(request,'Alquileres/alqui_oficinas.html',{ 'oficinas':oficinas})
def alqui_duplex(request):
    
    return render(request,'Alquileres/alqui_duplex.html')
def alqui_duplexdosdormi(request):
    duplexdosdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Duplex 2 Dormitorios"))
    return render(request,'Alquileres/alqui_duplexdosdormi.html',{ 'duplexdosdormis':duplexdosdormis})
def alqui_duplextresdormi(request):
    duplextresdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Duplex 3 Dormitorios"))
    return render(request,'Alquileres/alqui_duplextresdormi.html',{ 'duplextresdormis':duplextresdormis})
def alqui_casadosdormi(request):
    casadosdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 2 Dormitorios"))
    return render(request,'Alquileres/alqui_casadosdormi.html',{ 'casadosdormis':casadosdormis})
def alqui_casatresdormi(request):
    casatresdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 3 Dormitorios"))
    return render(request,'Alquileres/alqui_casatresdormi.html',{ 'casatresdormis':casatresdormis})

def alqui_casacuatrodormi(request):
    casacuatrodormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 4 Dormitorios"))
    return render(request,'Alquileres/alqui_casacuatrodormi.html',{ 'casacuatrodormis':casacuatrodormis})
def alqui_casacincodormi(request):
    casacincodormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Casas 5 Dormitorios"))
    return render(request,'Alquileres/alqui_casacincodormi.html',{ 'casacincodormis':casacincodormis})

def article(request,postalquiler_id):
    
    articles = get_object_or_404(PostAlquiler,pk=postalquiler_id)
    return render(request, 'Alquileres/alqui_post_detail.html',{'articles': articles})

def ofice_local_details_alqui(request,postalquiler_id):
    ofice_local_details_alquis = get_object_or_404(PostAlquiler,pk=postalquiler_id)
    return render(request, 'Alquileres/ofice_local_details_alqui.html',{'ofice_local_details_alquis': ofice_local_details_alquis})
def monoambiente_details_alqui(request, postalquiler_id):
    monoambiente_details_alqui = get_object_or_404(PostAlquiler, pk=postalquiler_id)
    return render (request,'Alquileres/monoambiente_details_alqui.html',{'monoambiente_details_alqui' : monoambiente_details_alqui})
