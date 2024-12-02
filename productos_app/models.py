from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.IntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    precio=models.PositiveSmallIntegerField()
    marca=models.CharField(max_length=100)
    stock=models.PositiveSmallIntegerField()
    descripcion=models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
