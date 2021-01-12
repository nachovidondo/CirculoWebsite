
from django.contrib import admin
from .models import Comprar,ComprarImagenes


class ComprarImagenesAdmin(admin.StackedInline):
    model = ComprarImagenes

@admin.register(Comprar)


class ComprarAdmin(admin.ModelAdmin):
    inlines=[ComprarImagenesAdmin]
    
    class Meta:
        model = Comprar
        

  

class ComprarImagenesAdmin(admin.ModelAdmin):
    pass
