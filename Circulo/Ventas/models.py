from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
 
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering= ["-created"]
    
    def __str__(self):
        return self.nombre
    
    
class Post(models.Model):
    title=  models.CharField(max_length=200, verbose_name="Titulo ")
    content = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", blank =True ,null =True,upload_to="Ventas")
    price = models.IntegerField(verbose_name="Precio")
    ambientes = models.IntegerField(verbose_name="Dormitorios o Ambientes",blank =True ,null =True)
    superficie= models.IntegerField(verbose_name="Superficie",blank =True,null =True )
    baños= models.IntegerField(verbose_name="Baños",blank = True,null =True)
    plantas= models.IntegerField(verbose_name="Plantas", blank = True,null =True)
    autor = models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
    
    class Meta:
            verbose_name="Publicacion"
            verbose_name_plural="Publicaciones"
            ordering= ["-created"]
    def __str__(self):
        return self.title

class PostImagenes(models.Model):
    
    post= models.ForeignKey(Post, default =None ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ="Imagenes",verbose_name="Imagenes") 
   
    class Meta:
        verbose_name="Agregar nueva Imagen"
        verbose_name_plural="Agregar nuevas Imagenes"
        def __str__(self):
            return self.post