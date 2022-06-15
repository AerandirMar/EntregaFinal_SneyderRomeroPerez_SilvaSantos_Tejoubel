from django.db import models


class Accion(models.Model):
    '''Aquí se agrega el nombre de la película, max 50 caracteres'''
    name = models.CharField(max_length=50)
    '''Se agrega la fecha de estreno en formato YYYY-MM-DD, aclarado en forms.py mediante widget'''
    fecha_estreno = models.DateField()
    '''Duración de la película en minutos'''
    duracion = models.IntegerField()
    '''Resumen de qué trata la película, no se pueden escribir más de 1.000 caracteres'''
    sinopsis = models.CharField(max_length=1000)


    def __str__(self):
        return f'{self.name} accion --'