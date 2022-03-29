"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'absence'

urlpatterns = [
    #path('', views.accueil, name='accueil'),
    #path('', views.contact_email, name='contact-email'),

    #path('', views.accueil, name='accueil'),

    #path('', views.formulaire, name='accueil-formulaire'),
    path('', views.formulaire, name='formulaire'),

    #path('se_connecter', views.se_connecter, name='se-connecter'),
    #path('creation_compte', views.creation_compte, name='creation-compte'),
    #path('connection_eleve', views.connection_eleve, name='connection-eleve'),
    #path('eleve', views.eleve, name='eleve'),

    #    Vue basée sur une vue de type classe : .as_view()
     #   path('eleve', views.eleve.as_view(), name='eleve'),
]

