from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    celular=models.PositiveSmallIntegerField()
    direccion=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre