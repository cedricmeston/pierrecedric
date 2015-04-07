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
    auteur= models.ForeignKey(User)
    slug = models.SlugField(max_length=100)
    contenu=models.TextField(null=True)
    date= models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie=models.ForeignKey('Categorie')
    prix=models.FloatField()
    typedeprix=models.ForeignKey('Typedeprix')

    def __str__(self):
        return self.titre


class Typedeprix(models.Model):
    nom=models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Reponse(models.Model):
    article=models.ForeignKey('Article')
    acheteur=models.ForeignKey(User)
    prix_acheteur=models.FloatField()
    type=models.ForeignKey('Typedeprix')
    commentaire=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'offre")
    def __str__(self):
        return self.article


class Categorie(models.Model):
    nom=models.CharField(max_length=30)

    def __str__(self):
        return self.nom

