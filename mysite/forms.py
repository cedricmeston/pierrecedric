from django import forms
from models import Article, User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('auteur',)

    def clean_author(self):
        if not self.cleaned_data['auteur']:
            return User()
        return self.cleaned_data['auteur']

    def clean_last_modified_by(self):
        if not self.cleaned_data['last_modified_by']:
            return User()
        return self.cleaned_data['last_modified_by']






class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur= forms.EmailField(label="Votre adresse mail")
    renvoi= forms.BooleanField(help_text="Cochez si vous voulez une reponse")

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
