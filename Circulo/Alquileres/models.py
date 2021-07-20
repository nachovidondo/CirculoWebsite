
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
    
    
class PostAlquiler(models.Model):
    balcon=(('Con Balcon','Con Balcon'),('Sin Balcon','Sin Balcon'))
    balcon = models.CharField(max_length=100, choices = balcon,default="Con Balcon", null=True, blank=True)
    frente= (('Externo','Externo'),('Contrafrente','Contrafrente'))
    frente = models.CharField(max_length=100,choices=frente, default = "Externo")
    title=  models.CharField(max_length=200, verbose_name="Titulo ")
    content = models.TextField(verbose_name="Contenido",max_length=800,)
    imagen = models.ImageField(verbose_name="Imagen", blank =True ,null =True,upload_to="Alquileres")
    price = models.IntegerField(verbose_name="Precio")
    ambientes = models.IntegerField(verbose_name="Dormitorios o Ambientes",blank =True ,null =True)
    superficie= models.IntegerField(verbose_name="Superficie (locales u oficinas)",blank =True,null =True )
    baños= models.IntegerField(verbose_name="Baños",blank = True,null =True)
    plantas= models.IntegerField(verbose_name="Plantas (locales u oficinas)", blank = True,null =True)
    autor = models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
    class Meta:
            verbose_name="Publicacion"
            verbose_name_plural="Plublicaciones"
            ordering= ["-created"]
    def __str__(self):
        return self.title

class PostImagenes(models.Model):
    post= models.ForeignKey(PostAlquiler, default =None ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ="Alquileres",verbose_name="Imagenes") 
    class Meta:
        verbose_name="Agregar una Imagen"
        verbose_name_plural="Agregar mas Imagenes"
        def __str__(self):
            return self.post.title
    
     