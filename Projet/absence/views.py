from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import VisiteurForm,Userform


from absence.models import Personne, service_secretariat,\
    Annee_scolaire, Classe, Eleve, Professeur, Matiere, \
    Presence

# Create your views here.

def accueil(request): # < here
    return render(request, 'accueil.html')
    #return render(request, 'accueil.html', {'section': 'contact'})

def formulaire(request):  # < here
    form = VisiteurForm(request.POST or None)
    form2 = Userform(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        form = VisiteurForm()
    mes_formulaires = {'form': form, 'form2': form2, }
    return render(request, 'formulaire.html' , mes_formulaires)



def se_connecter(request): # < here
    return render(request, 'se_connecter.html')

def creation_compte(request): # < here
    return render(request, 'creation_compte.html')

def connection_eleve(request): # < here
    if request.method == "POST":
        nom = request.POST['nom_eleve']
        prenom = request.POST['prenom_eleve']
        resultat_eleve = Eleve.objects.filter(nom = nom , prenom = prenom)
        if len(resultat_eleve) != 1 :
            messages.error(request,'Erreur d\'authentification')
            return render(request, 'connection.html')
        else :
            return render(request, 'eleve.html')
            #return redirect('eleve')
        #else:
         #   return render(request, 'eleve.html')
    #else :
     #   return HttpResponse('Veuillez vous connecter svp')
        #return redirect('accueil')
     #   return HttpResponse('Veuillez vous connecter svp')

#return HttpResponse('<H1>nom</H1>')

def eleve(request): # < here
    return render(request, 'eleve.html')

#def contact_email(request): # < here
 #  if request.method == "POST":
  #      nom = request.POST['name']
   #     return HttpResponse(nom)


# form = EleveForm(request)
# form = EleveForm(use_required_attribute=False)
# return render(request, 'formulaire.html' , {'form':form2})

''''
from django.shortcuts import render
from .forms import GeeksForm


# Create your views here.
def home_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("geeks_field")
            print(temp)
    return render(request, "home.html", context)


aaaaaaaaaa
'''''






