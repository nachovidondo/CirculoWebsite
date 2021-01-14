from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('alquiler/', views.alquiler ,name ="alquiler"),
    path('alqui_departamentos/', views.alqui_departamentos ,name ="alqui_departamentos"),
    path('alqui_monoambientes/', views.alqui_monoambientes ,name ="alqui_monoambientes"),
    path('alqui_dptoundormi/', views.alqui_dptoundormi ,name ="alqui_dptoundormi"),
    path('alqui_dptodosdormi/', views.alqui_dptodosdormi ,name ="alqui_dptodosdormi"),
    path('alqui_dptotresdormi/', views.alqui_dptotresdormi ,name ="alqui_dptotresdormi"),
    path('alqui_casas/', views.alqui_casas ,name ="alqui_casas"),
    path('alqui_locales/', views.alqui_locales ,name ="alqui_locales"),
    path('alqui_oficinas/', views.alqui_oficinas ,name ="alqui_oficinas"),

 
]
