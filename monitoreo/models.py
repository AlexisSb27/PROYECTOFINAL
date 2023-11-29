from django.db import models

class DatosContaminacion(models.Model):
    fecha = models.DateField()
    contaminante = models.CharField(max_length=100)
    nivel_contaminacion = models.FloatField()
    # Otros campos según tus necesidades

    def __str__(self):
        return self.contaminante
