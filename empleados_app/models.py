from django.db import models

# Create your models here.
class Empleado(models.Model):
    id=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    sueldo=models.PositiveSmallIntegerField()
    horario=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
