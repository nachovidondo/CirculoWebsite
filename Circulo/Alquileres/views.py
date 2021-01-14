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
