from django.db import models

# Create your models here.

class Cliente(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    celular=models.IntegerField()
    direccion=models.CharField(max_length=100)
    pedidos=models.IntegerField()
    fecha_inicio=models.DateField()

    def __str__(self):
        return self.nombre
