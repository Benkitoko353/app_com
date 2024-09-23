from django.db import models

# Create your models here.

class Categorie (models.Model):
    code = models.CharField(max_length=20,primary_key=True)
    libelle = models.CharField(max_length=15,null=False)
    
    def __str__(self):
        return self.libelle

class Produit (models.Model):
    code = models.CharField(max_length=20,primary_key=True)
    libelle = models.CharField(max_length=15,null=False)
    qte = models.IntegerField()
    pu = models.DecimalField(max_digits=5,decimal_places=2)
    Categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
