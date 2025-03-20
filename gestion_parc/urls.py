from django.urls import path


urlpatterns = [
    
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    # Liste des employés
    path('employes/', views.liste_employes, name='liste_employes'),
    
    # Détail d'un employé
    path('employe/<int:id>/', views.detail_employe, name='detail_employe'),
    path('employe/<int:id>/edite', views.modifier_employe, name='modifier_employe'),
    path('employe/<int:id>/supprimer', views.supprimer_employe, name='supprimer_employe'),
    
    # Liste des services
    path('services/', views.liste_services, name='liste_services'),
    path('services/<int:id>/', views.detail_service, name='detail_service'),
    path('services/<int:id>/edite', views.modifier_service, name='modifier_service'),
    path('services/<int:id>/supprimer', views.supprimer_service, name='supprimer_service'),
    
    
    # Liste des Antennes
    path('antennes/', views.liste_antennes, name='liste_antennes'),
    path('antennes/<int:id>/', views.detail_antenne, name='detail_antenne'),
    path('antennes/<int:id>/edite', views.modifier_antenne, name='modifier_antenne'),
    path('antennes/<int:id>/supprimer', views.supprimer_antenne, name='supprimer_antenne'),
    
    
    
    # Les équipements
    path('equipements/', views.liste_equipements, name='liste_equipements'),
    
    path('equipement/<int:id>/', views.detail_equipement, name='detail_equipement'),
    path('equipement/<int:id>/edite', views.modifier_equipement, name='modifier_equipement'),
    path('equipements/<int:id>/supprimer', views.supprimer_equipement, name='supprimer_equipement'),

    
    # # Historique des actions sur un équipement
    # path('historique/equipement/<int:equipement_id>/', views.historique_equipement, name='historique_equipement'),
    
    # Ajouter un nouvel employé
    path('employe/ajouter/', views.ajouter_employe, name='ajouter_employe'),
    
    # Ajouter un nouvel Service
    path('service/ajouter/', views.ajouter_service, name='ajouter_service'),
    
    # Ajouter un nouvel équipement
    path('equipement/ajouter/', views.ajouter_equipement, name='ajouter_equipement'),
    

    path('service/ajouter/', views.ajouter_service, name='ajouter_service'),
    
    # authentification route
    
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    # historique
    
    path('historique/', views.historique_list, name='historique_list'),
    path('historique/ajouter', views.ajouter_historique, name='ajouter_historique'),
    
    path('gestion_parc/setting', views.settings, name='settings'),
]
