from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Editorial(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) :
            return self.nombre
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    autor = models.CharField(max_length=20)
    numPag = models.IntegerField()
    formato = models.CharField(max_length=20)
    idEditorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    descripcion = models.TextField()
    #Borrar en caso de:
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class CarritoFunc(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)