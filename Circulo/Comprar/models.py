from django.db import models

# Create your models here.
class Comprar(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo ")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", blank =True )
    price = models.IntegerField(verbose_name="Precio")
    ambientes = models.IntegerField(verbose_name="Ambientes")
    superficie= models.IntegerField(verbose_name="Superficie")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Compra"
        verbose_name_plural="Compras"
        ordering= ["-created"]
    
class ComprarImagenes(models.Model):
    comprar = models.ForeignKey(Comprar,default =None ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ="Imagenes",verbose_name="Imagenes") 
    
    class Meta:
            verbose_name="Imagenes Compra"
    def __str__(self):
        return self.comprar