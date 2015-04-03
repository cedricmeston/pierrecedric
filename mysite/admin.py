from django.contrib import admin
from models import Categorie, Article, Typedeprix, Reponse




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = ('date')
    ordering = ('date',)
    search_fields = ('titre', 'contenu')

   # fieldsets = (
   #    ('General', {
   #         'classes': ['collapse', ],
   #         'fields': ('titre', 'slug', 'auteur', 'categorie')
   #     }),
   #     ('Contenu de l\'article', {
   #        'description': 'Le formulaire accepte les balises HTML. Utilisez les a bon escient !',
   #        'fields': ('contenu', )
   #     }),
   # )

    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.last_modified_by = request.user
        obj.save()

    def apercu_contenu(self, article):

        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return text
        else:
            return text

    apercu_contenu.short_description = 'Apercu du contenu'

admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Typedeprix)
admin.site.register(Reponse)
