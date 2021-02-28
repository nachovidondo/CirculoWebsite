from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('alquiler/', views.alquileres ,name ="alquiler"),
    path('alqui_departamentos/', views.alqui_departamentos ,name ="alqui_departamentos"),
    path('alqui_monoambientes/', views.alqui_monoambientes ,name ="alqui_monoambientes"),
    path('alqui_dptoundormi/', views.alqui_dptoundormi ,name ="alqui_dptoundormi"),
    path('alqui_dptodosdormi/', views.alqui_dptodosdormi ,name ="alqui_dptodosdormi"),
    path('alqui_dptotresdormi/', views.alqui_dptotresdormi ,name ="alqui_dptotresdormi"),
    path('alqui_casas/', views.alqui_casas ,name ="alqui_casas"),
    path('alqui_casadosdormi/', views.alqui_casadosdormi ,name ="alqui_casadosdormi"),
    path('alqui_casatresdormi/', views.alqui_casatresdormi ,name ="alqui_casatresdormi"),
    path('alqui_casacuatrodormi/', views.alqui_casacuatrodormi ,name ="alqui_casacuatrodormi"),
    path('alqui_casacincodormi/', views.alqui_casacincodormi ,name ="alqui_casacincodormi"),
    path('alqui_locales/', views.alqui_locales ,name ="alqui_locales"),
    path('alqui_oficinas/', views.alqui_oficinas ,name ="alqui_oficinas"),
    path('alqui_terrenos/', views.alqui_terrenos ,name ="alqui_terrenos"),
    path('alqui_duplex/', views.alqui_duplex ,name ="alqui_duplex"),
    path('alqui_duplexdosdormi/', views.alqui_duplexdosdormi ,name ="alqui_duplexdosdormi"),
    path('alqui_duplextresdormi/', views.alqui_duplextresdormi ,name ="alqui_duplextresdormi"),
    path('article/<int:postalquiler_id>/', views.article, name = "article"),
    path('ofice_local_details_alquis/<int:postalquiler_id>/', views.ofice_local_details_alquis, name = "ofice_local_details_alquis"),
    path('monoambiente_details_alquis/<int:postalquiler_id>/', views.monoambiente_details_alquis, name = "monoambiente_details_alquis")
    

]
