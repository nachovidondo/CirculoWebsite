from django.contrib import admin

from .models import Category,PostAlquiler, PostImagenes



 
class PostImagenesAdmin(admin.StackedInline):
    model = PostImagenes
    
@admin.register(PostAlquiler)


class PostAdmin(admin.ModelAdmin):
    inlines=[PostImagenesAdmin]
    
    class Meta:
        model = PostAlquiler

class AlquilerImagenesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)


 

  


