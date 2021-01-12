from django.shortcuts import render

# Create your views here.
def comprar(request):
    return render(request,'Comprar/comprar.html')