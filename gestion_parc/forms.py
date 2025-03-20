from django import forms
from .models import Equipement, Employe, Service, Antenne,  Historique

class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = ['nom', 'marque', 'serie', 'type', 'statut', 'utilisateur', 'service', 'antenne']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }
        
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'email', 'fonction', 'service', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["nom", "chef", "description", "antenne"]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'chef': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'antenne': forms.Select(attrs={'class': 'form-control'}),
        }
        
        

class AntenneForm(forms.ModelForm):
    class Meta:
        model = Antenne
        fields = ["nom", "ville", "chef_antenne"]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'chef_antenne': forms.TextInput(attrs={'class': 'form-control'}),
        }
        


class HistoriqueForm(forms.ModelForm):
    class Meta:
        model = Historique
        fields = ['employe', 'equipement', 'action', 'description']
        
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'equipement': forms.Select(attrs={'class': 'form-control'}),
            'action': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
