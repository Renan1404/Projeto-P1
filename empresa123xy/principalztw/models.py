from django.db import models

class Voos(models.Model):
    destino = models.CharField(max_length=30)
    horario = models.CharField(max_length=20)
    valorIda = models.FloatField(max_length=30)
    valorVolta = models.FloatField(max_length=20)
    companhia = models.CharField(max_length=30)

class Hotel(models.Model):
    Nome = models.CharField(max_length=20)
    CheckIn = models.DateField(max_length=30)
    CheckOut = models.DateField(max_length=20)
    valorHospedagem = models.FloatField(max_length=30)
    companhia = models.CharField(max_length=20)