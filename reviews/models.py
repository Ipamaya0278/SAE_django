from email.policy import default
from random import choices
from unicodedata import name
from django.db import models
from flask_sqlalchemy import Model
from datetime import datetime
from django.db import models

# Create your models here.

class Machine(models.Model):

    TYPE = (
        ('PC', ('PC - windows')),
        ('Linux', ('PC - Debian')),
        ('Serveur',('Serveur - Permet de deployer les machines virtuelles')),
        ('Switch', ('Switch - Connecte les serveurs entre eux ')),
    )
    TYPE2 = (
        ('Siege',('Poitiers')),
        ('Filiale',('Châtellerault')),
    )

    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(
        max_length=50
    )
    maintenanceDate = models.DateField( 
        default=datetime.now()
    )
    mach = models.CharField(
        max_length=32,
        choices=TYPE,
        default='PC'
    )
    infra = models.CharField(
        max_length=20,
        choices=TYPE2,
        default='Siege'
    )

    def __str__(self):
        return str(self.id) + " / " + self.nom  +  " / " + self.infra

    def get_name(self): 
        return str(self.id) + " " + self.nom

class Personnel(models.Model):

    TYPE = (
        ('Siege',('Poitiers')),
        ('Filiale',('Châtellerault')),
    )
    TYPE2 = (
        ('Employe',('Filiale')),
        ('Manager',('Siege')),
    )
    num_secu =models.CharField(
        primary_key=True,
        editable=True,
        max_length = 15
    )
    nom = models.CharField(
        max_length=50
    )
    prenom = models.CharField(
        max_length=50
    )
    personne = models.CharField(
        max_length=20,
        choices=TYPE2,
        default='Employe'
    )
    infra = models.CharField(
        max_length=20,
        choices=TYPE,
        default='Siege'
    )
    mach = models.ForeignKey(Machine, default=None, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.num_secu )+ "  /  " + self.nom + "  /  " + self.prenom + "  /  " + self.infra


status_choice = (('approved','APPROVED'),('pending','PENDING'),('rejected','REJECTED'))


class Review(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    status = models.CharField(
            max_length=10,choices=status_choice,default='pending'
        )
    nom = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    mach = models.ForeignKey(Machine,default=None, null=True, on_delete=models.SET_NULL)
    maintenanceDate = models.DateTimeField()
    
    def __str__(self):
        return self.nom.mach 

