from django.db import models

class Universidad_de_Buenos_Aires(models.Model):
    facultad= models.CharField(max_length=100)
    carrera= models.CharField(max_length=100)

    def __str__(self):
        return f'UBA({self.id}): {self.facultad} - {self.carrera}'