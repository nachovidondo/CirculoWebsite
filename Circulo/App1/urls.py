from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.inicio, name = "inicio"),
    path('articulos/<int:postinicio_id>/',views.articulos, name = "articulos")
]
