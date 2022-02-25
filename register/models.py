from django.db import models

# Create your models here.
class Integrante(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class ObjectiveKeyResult(models.Model):
    integrante = models.ForeignKey(Integrante, related_name='okrs', on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=200)
    resultado_1 = models.CharField(max_length=300, null=False)
    resultado_2 = models.CharField(max_length=300, null=False, blank=True)
    resultado_3 = models.CharField(max_length=300, null=False, blank=True)
    resultado_4 = models.CharField(max_length=300, null=False, blank=True)
    resultado_5 = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.objetivo
