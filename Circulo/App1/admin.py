from django.contrib import admin
from .models import Inicio 
# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    readonly_fields= ["created","updated"]
    
admin.site.register(Inicio,InicioAdmin)