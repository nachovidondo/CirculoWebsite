from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto ,name ="contacto"),
    path('automatic/',views.automatic, name  ="automatic"),
    path('tasaciones/', views.tasaciones ,name ="tasaciones"),

 
]
