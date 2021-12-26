from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=30, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url_demo = models.URLField(null=True, blank=True, verbose_name="Link de la demostracion del Sitio")
    url_github_user = models.URLField(null=True, blank=True, verbose_name="Link de la cuenta del usuario en Github")
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        
    def __str__(self):
        return self.title