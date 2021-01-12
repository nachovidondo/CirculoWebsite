from django.shortcuts import render

# Create your views here.
def alquiler(request):
    return render (request, 'Alquilar/alquiler.html')