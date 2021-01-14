from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('ventas/', views.ventas ,name ="ventas"),
    path('venta_departamentos/', views.venta_departamentos ,name ="venta_departamentos"),
    path('venta_monoambientes/', views.venta_monoambientes ,name ="venta_monoambientes"),
    path('venta_dptoundormi/', views.venta_dptoundormi ,name ="venta_dptoundormi"),
    path('venta_dptodosdormi/', views.venta_dptodosdormi ,name ="venta_dptodosdormi"),
    path('venta_dptotresdormi/', views.venta_dptotresdormi ,name ="venta_dptotresdormi"),
    path('venta_casas/', views.venta_casas ,name ="venta_casas"),
    path('venta_locales/', views.venta_locales ,name ="venta_locales"),
    path('venta_oficinas/', views.venta_oficinas ,name ="venta_oficinas"),
    path('venta_terrenos/', views.venta_terrenos ,name ="venta_terrenos"),

]
