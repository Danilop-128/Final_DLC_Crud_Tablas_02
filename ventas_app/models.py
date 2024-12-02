from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.IntegerField(primary_key=True)
    id_empleado=models.CharField(max_length=100)
    id_cliente=models.IntegerField(max_length=100)
    id_producto=models.IntegerField(max_length=100)
    fecha_venta=models.DateField(max_length=100)
    cantidad=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return self.id_empleado
