from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')

def propiedades(request):
    return render(request,'App1/propiedades.html')