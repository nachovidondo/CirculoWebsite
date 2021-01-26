from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('tasaciones/', views.tasaciones ,name ="tasaciones"),
    path('acercanuestro/',views.acercanuestro, name  ="acercanuestro"),
    path('articulo/<int:postinicio_id>/', views.articulo, name = "articulo")
]
