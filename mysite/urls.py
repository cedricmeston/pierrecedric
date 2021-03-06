from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns(
    "mysite.views",
    url(r"^$", 'accueil', name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'lire'),
    url(r'^contact/$', 'contact'),
    url(r'^nouveau/$', 'nouveau'),
    url(r'^reponse/(?P<id>\d+)-(?P<slug>.+)$', 'reponse'),
    url(r'^categorie/(?P<id>\d+)$', 'categorie'),
    url(r"^search/$", 'search'),
    url(r'^lire_reponses$', 'lire_reponses'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
