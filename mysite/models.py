from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User)
    adresse = models.TextField()
    ville = models.TextField(max_length=100)
    code_postal = models.FloatField()
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    date_naissance = models.DateField()
    nom = models.TextField()
    prenom = models.TextField()

    def __str__(self):
        return self.user

class Article(models.Model):
    titre= models.CharField(max_length=100)
    auteur= models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu=models.TextField(null=True)
    date= models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie=models.ForeignKey('Categorie')
    prix=models.OneToOneField('Prix')

    def __str__(self):
        return self.titre

class Prix(models.Model):
    type=models.ForeignKey('Type_de_prix')
    valeur=models.FloatField()

class Type_de_prix(models.Model):
    nom=models.CharField(max_length=100)

class Reponse(models.Model):
    article=models.ForeignKey('Article')
    acheteur=models.ForeignKey('Profil')
    prix_acheteur=models.FloatField()
    type=models.ForeignKey('Type_de_prix')
    commentaire=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'offre")


class Categorie(models.Model):
    nom=models.CharField(max_length=30)

    def __str__(self):
        return self.nom

