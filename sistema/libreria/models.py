from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagen', null=True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    
    def __str__(self):
        fila = "Titulo:" + self.titulo + "desripcion:" + self.descripcion 
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()