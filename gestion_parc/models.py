from django.db import models
from django.contrib.auth.models import User






class Antenne(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    ville = models.CharField(max_length=100)
    chef_antenne = models.CharField(max_length=110, unique=True)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    chef = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    antenne = models.ForeignKey(Antenne, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.antenne.nom}"


class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fonction = models.CharField(max_length=150)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Equipement(models.Model):
    TYPE_CHOICES = [
        ('ordinateur', 'Ordinateur'),
        ('imprimante', 'Imprimante'),
        ('serveur', 'Serveur'),
        ('autre', 'Autre'),
    ]
    
    statut_choices = [
        ('actif', 'Actif'),
        ('en_reparation', 'En réparation'),
        ('hors_service', 'Hors service'),
        ('reserve', 'Réservé'),
    ]

    nom = models.CharField(max_length=100)
    marque = models.CharField(max_length=50)
    serie = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    statut = models.CharField(max_length=50, choices=statut_choices, default='actif')
    utilisateur = models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    antenne = models.ForeignKey(Antenne, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} ({self.type})"


class Historique(models.Model):
    ACTION_CHOICES = [
        ('ATTRIBUTION', 'Attribution'),
        ('RETOUR', 'Retour'),
        ('MAINTENANCE', 'Maintenance'),
        ('REPARATION', 'Réparation'),
        ('SUPPRESSION', 'Suppression'),
    ]

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    date_action = models.DateTimeField(auto_now_add=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.action} sur {self.equipement.nom} par {self.employe.nom} le {self.date_action.strftime('%Y-%m-%d %H:%M:%S')}"

