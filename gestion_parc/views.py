from django.shortcuts import render, get_object_or_404, redirect
from .models import Employe, Service, Equipement, Historique, Antenne
from django.http import HttpResponse
from .forms import EquipementForm, EmployeForm, ServiceForm, AntenneForm, HistoriqueForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse



@login_required
def ajouter_historique(request):
    if request.method == 'POST':
        form = HistoriqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historique_list')
    else:
        form = HistoriqueForm()
    
    return render(request, 'gestion_parc/ajouter_historique.html', {'form': form})



@login_required
def home(request):
    
    nombre_employe = Employe.objects.all().count()
    nombre_equipements = Equipement.objects.all().count()
    nombre_antennes = Antenne.objects.all().count()
    historique_recent = Historique.objects.all().order_by('date_action').count()
    
    
    return render(request, 'gestion_parc/dashboard.html', locals())


# Liste des employés
@login_required
def liste_employes(request):
    employes = Employe.objects.all()
    paginator = Paginator(employes, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'gestion_parc/liste_employes.html', {'employes': employes, "page_obj": page_obj})

# Détail d'un employé
@login_required
def detail_employe(request, id):
    employe = get_object_or_404(Employe, pk=id)
    return render(request, 'gestion_parc/detail_employe.html', {'employe': employe})

# Liste des services
@login_required
def liste_services(request):
    services = Service.objects.all()
    return render(request, 'gestion_parc/liste_services.html', {'services': services})

# Détail d'un service
@login_required
def detail_service(request, id):
    service = get_object_or_404(Service, pk=id)
    employe_service = Employe.objects.filter(service=id)
    return render(request, 'gestion_parc/detail_service.html', {'service': service, 'employes': employe_service})

# Liste des équipements
@login_required
def liste_equipements(request):
    equipements = Equipement.objects.all()
    paginator = Paginator(equipements, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'gestion_parc/liste_equipements.html', {'equipements': equipements, "page_obj": page_obj})

# Détail d'un équipement
@login_required
def detail_equipement(request, id):
    equipement = get_object_or_404(Equipement, pk=id)
    historique = Historique.objects.filter(equipement=equipement)
    return render(request, 'gestion_parc/detail_equipement.html', {'equipement': equipement, 'historique': historique})


@login_required
def historique_list(request):
    historiques = Historique.objects.all().order_by('-date_action')

    # Récupérer les filtres depuis la requête GET
    employe_id = request.GET.get('employe')
    equipement_id = request.GET.get('equipement')
    action = request.GET.get('action')

    if employe_id:
        historiques = historiques.filter(employe__id=employe_id)
    if equipement_id:
        historiques = historiques.filter(equipement__id=equipement_id)
    if action:
        historiques = historiques.filter(action=action)

    # Pagination : 10 résultats par page
    paginator = Paginator(historiques, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gestion_parc/historique_list.html', {'page_obj': page_obj})


# Ajouter un employé
@login_required
def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_employes')
    else:
        form = EmployeForm()
    
    return render(request, 'gestion_parc/ajouter_employes.html', {'form': form})

# Ajouter un équipement
@login_required
def ajouter_equipement(request):
    if request.method == "POST":
        form = EquipementForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('liste_equipements')

    else:
        form = EquipementForm()
        
    return render(request, 'gestion_parc/ajouter_equipement.html', {"form": form})







@login_required
def ajouter_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('liste_services')

    else:
        form = ServiceForm()
        
    return render(request, 'gestion_parc/ajouter_service.html', {"form": form})






# modification views
@login_required
def modifier_equipement(request, id):
    equipement = get_object_or_404(Equipement, pk=id)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            messages.success(request, "L'equipement à été modifié avec succès")
            return redirect('liste_equipements')  # Remplacez 'equipement_liste' par votre vue de liste d'équipements
    else:
        form = EquipementForm(instance=equipement)
          
    return render(request, 'gestion_parc/modifier_equipement.html', {'form': form})



@login_required
def modifier_employe(request, id):
    employe = get_object_or_404(Employe, pk=id)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            messages.success(request, "L'employé à été modifié avec succès")
            return redirect('liste_employes')
    else:
        form = EmployeForm(instance=employe)
    
    return render(request, 'gestion_parc/modifier_employe.html', {'form': form})


@login_required
def modifier_service(request, id):
    service = get_object_or_404(Service, pk=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Le service à été modifié avec succès")
            return redirect('liste_services')
    else:
        form = ServiceForm(instance=service)
    
    return render(request, 'gestion_parc/modifier_service.html', {'form': form})



# suppression views

@login_required
def supprimer_equipement(request, id):
    equipement = get_object_or_404(Equipement, pk=id)
    
    if request.method == "POST":
        equipement.delete()
        messages.success(request, "Équipement supprimé avec succès !")
        return redirect('liste_equipements')

    return render(request, 'gestion_parc/supprimer_equipement.html', {'equipement': equipement})



@login_required
def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, pk=id)
    
    if request.method == "POST":
        employe.delete()
        messages.success(request, "Employé supprimé avec succès !")
        return redirect('liste_employes')

    return render(request, 'gestion_parc/supprimer_employe.html', {'employe': employe})


@login_required
def supprimer_service(request, id):
    service = get_object_or_404(Service, pk=id)
    if request.method == "POST":
        service.delete()
        messages.success(request, "Service supprimé avec succès !")
        return redirect('liste_services')

    return render(request, 'gestion_parc/supprimer_service.html', {'service': service})




# antenne
# Liste des équipements
@login_required
def liste_antennes(request):
    antennes = Antenne.objects.all()
    return render(request, 'gestion_parc/liste_antennes.html', {'antennes': antennes})




# Détail d'un équipement
@login_required
def detail_antenne(request, id):
    antenne = get_object_or_404(Antenne, pk=id)
    services = Service.objects.filter(pk=id)
    return render(request, 'gestion_parc/detail_antenne.html', {'antenne': antenne, 'services': services})

@login_required
def supprimer_antenne(request, id):
    antenne = get_object_or_404(Antenne, pk=id)
    if request.method == "POST":
        antenne.delete()
        messages.success(request, "antenne supprimé avec succès !")
        return redirect('liste_antennes')

    return render(request, 'gestion_parc/supprimer_antenne.html', {'antenne': antenne})

@login_required
def modifier_antenne(request, id):
    antenne = get_object_or_404(Antenne, pk=id)
    if request.method == 'POST':
        form = AntenneForm(request.POST, instance=antenne)
        if form.is_valid():
            form.save()
            messages.success(request, "L'antenne à été modifié avec succès")
            return redirect('liste_antennes')
    else:
        form = AntenneForm(instance=antenne)
    
    return render(request, 'gestion_parc/modifier_antenne.html', {'form': form})












# authentification

def inscription(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie !")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/inscription.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    messages.info(request, "Déconnexion réussie.")
    return redirect('connexion')

def settings(request):
    # Cette vue peut inclure des paramètres pour l'utilisateur ou des configurations globales
    return render(request, 'gestion_parc/settings.html')