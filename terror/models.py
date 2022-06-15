from django.db import models


class Terror(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()
    sinopsis = models.CharField(max_length=1000)


    def __str__(self):
        return f'{self.name} terror --'