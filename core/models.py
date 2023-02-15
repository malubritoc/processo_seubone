from django.db import models

class Tecido(models.Model):
    referencia = models.CharField(max_length=10)
    tipo = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    metragem = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.tipo} - {self.cor}'

