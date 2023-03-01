from django.db import models

# Create your models here.
class CVE(models.Model):
    """Modelo para la base de datos de las vulnerabilidades"""
    id=models.CharField(primary_key=True,max_length=50)
    solucionado = models.BooleanField(default=False)
    publicado= models.DateTimeField()
    ultimaModificacion= models.DateTimeField()
    descripcion = models.TextField(max_length=500)
    severidad = models.CharField(max_length=50)
    estado=models.CharField(max_length=50)





