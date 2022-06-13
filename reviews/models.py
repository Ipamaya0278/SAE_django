from email.policy import default
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
        return str(self.id) + " -> " + self.nom

    def get_name(self): 
        return str(self.id) + " " + self.nom

class Personnel(models.Model):

    TYPE = (
        ('Siege',('Poitiers')),
        ('Filiale',('Châtellerault')),
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
    infra = models.CharField(
        max_length=20,
        choices=TYPE,
        default='Siege'
    )
    def __str__(self):
        return str(self.num_secu) + "  /  " + self.nom + "  /  " + self.prenom



status_choice = (('approved','APPROVED'),('pending','PENDING'),('rejected','REJECTED'))


class Review(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    status = models.CharField(
            max_length=10,choices=status_choice,default='pending'
        )
    nom = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    mach = models.ForeignKey(Machine, on_delete=models.CASCADE)
    maintenanceDate = models.DateTimeField()
    
    def __str__(self):
        return self.nom.mach 

