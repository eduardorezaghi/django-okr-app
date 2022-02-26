from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Integrante(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class ObjectiveKeyResult(models.Model):
    text = RegexValidator(r'^[0-9a-zA-Z]*$', 'Só é permitido números e letras.')

    integrante = models.ForeignKey(Integrante, related_name='okrs', on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=200, validators=[text])
    resultado_1 = models.CharField(max_length=300, null=False, validators=[text])
    resultado_2 = models.CharField(max_length=300, null=False, blank=True, validators=[text])
    resultado_3 = models.CharField(max_length=300, null=False, blank=True, validators=[text])
    resultado_4 = models.CharField(max_length=300, null=False, blank=True, validators=[text])
    resultado_5 = models.CharField(max_length=300, null=False, blank=True, validators=[text])

    def __str__(self):
        return self.objetivo
