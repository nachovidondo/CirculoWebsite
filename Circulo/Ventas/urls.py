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
    path('venta_casadosdormi/', views.venta_casadosdormi ,name ="venta_casadosdormi"),
    path('venta_casatresdormi/', views.venta_casatresdormi ,name ="venta_casatresdormi"),
    path('venta_casacuatrodormi/', views.venta_casacuatrodormi ,name ="venta_casacuatrodormi"),
    path('venta_casacincodormi/', views.venta_casacincodormi ,name ="venta_casacincodormi"),
    path('venta_locales/', views.venta_locales ,name ="venta_locales"),
    path('venta_oficinas/', views.venta_oficinas ,name ="venta_oficinas"),
    path('venta_terrenos/', views.venta_terrenos ,name ="venta_terrenos"),
    path('venta_duplex/', views.venta_duplex ,name ="venta_duplex"),
    path('venta_duplexdosdormi/', views.venta_duplexdosdormi ,name ="venta_duplexdosdormi"),
    path('venta_duplextresdormi/', views.venta_duplextresdormi ,name ="venta_duplextresdormi"),
    path('articulos_venta/<int:post_id>/', views.articulos_venta, name = "articulos_venta"),
    path('ofice_local_details_ventas/<int:post_id>/', views.ofice_local_details_ventas, name = "ofice_local_details_ventas"),
    path('monoambiente_details_ventas/<int:post_id>/', views.monoambiente_details_ventas, name = "monoambiente_details_ventas")
    

]
