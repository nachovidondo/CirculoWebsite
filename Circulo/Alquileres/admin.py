from django.contrib import admin
from .models import Category,PostAlquiler, PostImagenes

class PostImagenesAdmin(admin.StackedInline):
    model = PostImagenes
    
@admin.register(PostAlquiler)


class PostAdmin(admin.ModelAdmin):
    inlines=[PostImagenesAdmin]
    readonly_fields=["created","updated","imagen"]
    list_display=("title","created","autor")
    ordering=("autor",)
    search_fields=("title","autor__username")
    list_filter=("title","autor__username")

    
    class Meta:
        model = PostAlquiler

class AlquilerImagenesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
