from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User)
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Article(models.Model):
    titre= models.CharField(max_length=100)
    auteur= models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu=models.TextField(null=True)
    date= models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie=models.ForeignKey('Categorie')



    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom=models.CharField(max_length=30)

    def __str__(self):
        return self.nom

