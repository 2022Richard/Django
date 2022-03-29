#from django.forms import ModelForm
from django import forms
from .models import Classe, Eleve, Visiteur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
#from django.http import Http404
"""
Une classe pour les forms en utilisant le modèle User : from django.contrib.auth.forms import UserCreationForm
"""


class VisiteurForm(forms.ModelForm):
    nom = forms.CharField(required=False,error_messages =({'required' : 'Obligatoire'}),widget=forms.TextInput(attrs={'placeholder': 'Entrer votre nom ici', }))
    prenom = forms.CharField(label = 'prénom',required=False, widget=forms.TextInput(attrs={'placeholder': 'Entrer votre prenom ici',}))

    class Meta :
        model = Visiteur
        #model : Eleve
        fields =['nom', 'prenom']

    def clean_nom(self, *args, **kwargs):
        #print(type(self.cleaned_data.get('nom')))
        Newnom = self.cleaned_data.get("nom")
        #print('Hello')
        if Newnom is not None :
            return Newnom
        else:
            raise forms.ValidationError('Ce champ ne doit pas être vide')




class Userform(forms.ModelForm):

    mon_profil = (('Eleve', 'Eleve'), ('Professeur', 'Professeur'),('Service secretariat','Service secretariat'))
    username = forms.CharField(label ='Login', required=False, widget=forms.TextInput(attrs={'placeholder': 'Choisissez un login, vous en aurez besoin pour vous connecter','required':''}))
    email = forms.EmailField(label ='Email',required=False, widget=forms.TextInput(attrs={'placeholder': 'Entrer votre email ici','required':''}))
    password1 = forms.CharField(label ='Mot de passe',required=False, widget=forms.PasswordInput(attrs={'placeholder': '','required':''}))
    password2 = forms.CharField(label ='Confirmation mot de passe',required=False, widget=forms.PasswordInput(attrs={'placeholder': '','required':''}))
    choix_profil = forms.CharField(label='Choisissez votre profil',required=False, widget=forms.Select(choices = mon_profil))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





'''''       
class ClasseForm(ModelForm):
    class Meta :
        model = Classe
        #fields = ('nom', 'annee_scolaire',)
        fields ='__all__'
        
class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']        
'''''