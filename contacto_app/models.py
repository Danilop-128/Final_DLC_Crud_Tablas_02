from django.db import models

# Create your models here.
class Contacto(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    celular=models.PositiveSmallIntegerField()
    direccion=models.CharField(max_length=100)
    url_web=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre