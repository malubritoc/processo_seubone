from django.db import models

class Tecido(models.Model):
    tipo = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    #descobrir como faz p colocar numero
    metragem = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.tipo} - {self.cor}'