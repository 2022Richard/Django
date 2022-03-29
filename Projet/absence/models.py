from django.db import models

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

class service_secretariat(Personne) :
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Annee_scolaire(models.Model) :
    annee_scolaire = models.CharField(max_length=11)
    def __str__(self):
        return self.annee_scolaire

class Classe(models.Model) :
    nom = models.CharField(max_length=80)
    annee_scolaire = models.ForeignKey(Annee_scolaire, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Eleve(Personne) :
    titre = (('Chef', 'Chef de classe'), ('Autre', 'Autre'))
    statut = models.CharField(max_length=30, choices=titre, default='autre')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

class Professeur(Personne) :
    classe = models.ManyToManyField(Classe)

class Matiere(models.Model) :
    nom = models.CharField(max_length=80)
    eleve = models.ManyToManyField(Eleve, through='Presence')
    #professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Presence(models.Model) :
    statut = (('P', 'present'), ('A', 'absent'))
    heure = (('8H-10H','8H-10H'),('10H15-12H15','10H15-12H15'),('13H30-15H30','13H30-15H30'),
             ('15H30-17H30','15H30-17H30'),('17H30-19H30','17H30-19H30'))
    presence = models.CharField(max_length=1, null=True, choices=statut)
    date = models.DateField(auto_now_add=True)
    heures_cours = models.CharField(max_length=30, choices=heure, default='8H-10H')
    Matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

    #matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    #eleve = models.ManyToManyField(Eleve)

#return '%s %s' % (self.first_name, self.last_name)

class Visiteur(Personne) :
    pass

'''''
Je suis un commentaire
'''''



