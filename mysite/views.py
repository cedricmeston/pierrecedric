from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from models import Article, Categorie
from forms import ContactForm, ArticleForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from snipped import get_query

def accueil(request):
    articles = Article.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'accueil.html', {'derniers_articles': articles, 'liste_categories': categories})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['titre', 'contenu',])

        found_entries = Article.objects.filter(entry_query).order_by('date')

    return render_to_response('search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'lire.html', {'article':article})

def categorie(request, id):
    categorie1 = get_object_or_404(Categorie, id=id)
    articles=  categorie1.article_set.all()
    return render(request, 'categorie.html', {'categorie': categorie1, 'liste_articles': articles})


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

