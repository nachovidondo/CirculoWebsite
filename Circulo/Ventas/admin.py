from django.contrib import admin

from .models import Category,Post, PostImagenes



 
class PostImagenesAdmin(admin.StackedInline):
    model = PostImagenes
    
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    inlines=[PostImagenesAdmin]
    
    class Meta:
        model = Post

class AlquilerImagenesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)


 

  



    


