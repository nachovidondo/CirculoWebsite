from django.db import models

# Create your models here.
class Inicio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo ")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", blank =True ,upload_to="Inicio")
    precio = models.IntegerField(verbose_name="Precio")
    ambientes = models.IntegerField(verbose_name="Dormitorios")
    superficie= models.IntegerField(verbose_name="Superficie")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Pagina de Inicio"
        verbose_name_plural="Paginas de inicio"
        ordering= ["-created"]
    