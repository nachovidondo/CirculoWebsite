from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio ,name ="inicio"),
    path('propiedades/', views.propiedades ,name ="propiedades"),
]
