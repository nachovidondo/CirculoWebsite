from django.contrib import admin

from .models import Category,Post, PostImagenes



 
class PostImagenesAdmin(admin.StackedInline):
    model = PostImagenes
    
@admin.register(Post)



class PostAdmin(admin.ModelAdmin):
    inlines=[PostImagenesAdmin]
    readonly_fields=["created","updated","imagen"]
    list_display=("title","created","autor")
    ordering=("autor",)
    search_fields=("title","autor__username")
    list_filter=("title","autor__username")
    
    class Meta:
        model = Post

class VentasImagenesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)


 

  



    


