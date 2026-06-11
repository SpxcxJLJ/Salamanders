from django.db import models

# Create your models here.
from django.db import models

class Composition(models.Model):
    promotion = models.CharField(max_length=50)
    date_creation = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    date_fin = models.DateField(null=True, blank=True)

class CompositionDetail(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE, related_name="details")
    id_matiere = models.IntegerField()
    id_enseignant = models.IntegerField()
    coefficient = models.FloatField()
    volume_horaire = models.FloatField()
    ordre = models.IntegerField(default=0)
    class Meta:
        ordering = ['ordre']
class RapportEtudiant(models.Model):
    numero_etudiant = models.IntegerField()
    periode_debut = models.DateField()
    periode_fin = models.DateField()
    heures_totales = models.FloatField(default=0)

class RapportEnseignant(models.Model):
    id_enseignant = models.IntegerField()
    periode_debut = models.DateField()
    periode_fin = models.DateField()
    heures_totales = models.FloatField(default=0)