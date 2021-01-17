from django.shortcuts import render
from . models import PostAlquiler, Category

# Create your views here.
def alquiler(request):
    return render (request,'Alquileres/alquiler.html')
    

def alqui_monoambientes(request):
    monoambientes=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Monoambientes"))
    
    return render (request, 'Alquileres/alqui_monoambientes.html',{ 'monoambientes' : monoambientes })

def alqui_departamentos(request):
    return render(request,'Alquileres/alqui_departamentos.html')

def alqui_dptoundormi(request):
    dptoundormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "1 Dormitorio"))
    
    return render (request, 'Alquileres/alqui_dptoundormi.html',{ 'dptoundormis' : dptoundormis })

def alqui_dptodosdormi(request):
    dptodosdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "2 Dormitorios"))
    return render(request,'Alquileres/alqui_dptodosdormi.html',{ 'dptodosdormis':dptodosdormis})




def alqui_dptotresdormi(request):
    dptotresdormis=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "3 Dormitorios"))
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
    duplex=PostAlquiler.objects.filter(categories=Category.objects.get(nombre = "Duplex"))
    return render(request,'Alquileres/alqui_duplex.html',{ 'duplex':duplex})
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
