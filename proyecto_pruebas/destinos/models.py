from django.db import models

# Create your models here.
class Destino(models.Model):
    iden = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    explicacion = models.TextField()
    imagen = models.ImageField(upload_to='destinos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'

    def __str__(self):
        return self.nombre