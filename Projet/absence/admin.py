from django.contrib import admin

# Register your models here.

from absence.models import Personne, service_secretariat,Annee_scolaire, Classe, Eleve, Professeur, Matiere, Presence

#admin.site.register(Personne)
admin.site.register(service_secretariat)
admin.site.register(Annee_scolaire)
admin.site.register(Classe)
admin.site.register(Eleve)
admin.site.register(Professeur)
admin.site.register(Matiere)
admin.site.register(Presence)
#admin.site.register(Personne)
