from django.contrib import admin
from .models import Alquilar, AlquilarImagenes
# Register your models here.
class AlquilarImagenesAdmin(admin.StackedInline):
    model = AlquilarImagenes
    
@admin.register(Alquilar)


class AlquilarAdmin(admin.ModelAdmin):
    inlines=[AlquilarImagenesAdmin]
    
    class Meta:
        model = Alquilar

class AlquilerImagenesAdmin(admin.ModelAdmin):
    pass
        

  

