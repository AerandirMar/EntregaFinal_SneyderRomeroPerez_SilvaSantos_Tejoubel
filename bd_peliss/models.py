from django.db import models


from django.db import models


class Accion(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()
    sinopsis = models.CharField(max_length=1000)


class Terror(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()
    sinopsis = models.CharField(max_length=1000)


class Comedia(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()
    sinopsis = models.CharField(max_length=1000)


class CienciaFiccion(models.Model):
    name = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    duracion = models.IntegerField()
    sinopsis = models.CharField(max_length=1000)