from django.db import models

class Universidad_de_Buenos_Aires(models.Model):
    facultad= models.CharField(max_length=100)
    carrera= models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="imagenes_uba", null=True)

    def __str__(self):
        return f'({self.id}): {self.facultad} - {self.carrera}'