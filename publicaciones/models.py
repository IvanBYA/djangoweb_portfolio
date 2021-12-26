from django.db import models

# Create your models here.

class publication(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="publications")
    url = models.URLField(null=True, blank=True, verbose_name="link del sitio")
    
    class Meta:
        verbose_name = "publicacion"
        verbose_name_plural = "publicaciones"
    
    def __str__(self):
        return self.title
