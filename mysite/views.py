from django.shortcuts import render, get_object_or_404, redirect
from models import Article, Categorie
from forms import ContactForm, ArticleForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def accueil(request):
    articles = Article.objects.all()
    return render(request, 'accueil.html', {'derniers_articles' : articles})


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'lire.html', {'article':article})


def contact(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)

        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            envoi= True
    else:
        form = ContactForm()

    return render(request, 'contact.html', locals())

@login_required()
def nouveau(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
            form.save()
            envoi= True
    else:
        form = ArticleForm()

    return render(request, 'nouveau.html', locals())

@login_required()
def modifier(request, id, slug):
     article = get_object_or_404(Article, id=id, slug=slug)
     form = ArticleForm(request.POST, instance=article)
     if form.is_valid():
            form.save()
            article = form.save()
            article.save()
            envoi= True
     else:
        form = ArticleForm(instance=article)

     return render(request, 'modifier.html', locals() )

