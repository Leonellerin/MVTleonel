from django.db import models

class Padre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=40)


class Madre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField


class Hermano(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField
