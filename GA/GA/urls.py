"""
URL configuration for GA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from gestionga import views 
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home' ,views.home, name= "home"),
    path('ajoutdomaine',views.ajout_domaine, name = "ajoutdomaine"),
    path('deletedomaine/<int:id>',views.delete_domaine, name = "deletedomaine"),
    path('updatedomaine/<int:id>',views.update_domaine, name = "updatedomaine"),
    path('ajoutprogramme',views.ajout_programme, name = "ajoutprogramme"),
    path('deleteprogramme/<int:id>',views.delete_programme, name = "deleteprogramme"),
    path('updateprogramme/<int:id>',views.update_programme, name = "updateprogramme"),
    path('ajoutprofil',views.ajout_profil, name = "ajoutprofil"),
    path('deleteprofil/<int:id>',views.delete_profil, name = "deleteprofil"),
    path('updateprofil/<int:id>',views.update_profil, name = "updateprofil"),
    path('ajoutdroit',views.ajout_droit, name = "ajoutdroit"),
    path('ajouthabilitation',views.ajout_habilitation, name = "ajouthabilitation"),
    path('deletehabilitation/<int:id>',views.delete_habilitation, name = "deletehabilitation"),
    path('updatehabilitation/<int:id>',views.update_habilitation, name = "updatehabilitation"),
    path('FonctionRechercheProgramme', views.faire_rechercheprogramme, name='FonctionRechercheProgramme'), #fonction de recherche programme
    path('rechercheprogramme',views.faire_rechercheprogramme, name = "rechercheprogramme"), # appel de la page de recherche de programme
    path('tableau_ressource',views.recup_ressource, name = "tableau_ressource"),
    path('ajouterressource',views.enregistrer_ressource, name = "ajouterressource"),
    path('programmeabsent',views.rechercher_programmes_absents, name = "programmeabsent"), # page pour rechercher les programmes absents
    path('FonctionProgrammeAbsent',views.rechercher_programmes_absents, name = "FonctionProgrammeAbsent"), # appel de la fonction de traitement programmes absents
    path('ajoutapplication',views.ajout_appli, name = "ajoutapplication"),
    path('programmega',views.recherche_programme_GA, name = "programmega"),
    path('fonctionprogrammega',views.recherche_programme_GA, name = "fonctionprogrammega"),
    path('telecharger_en_excel', views.telecharger_en_excel, name='telecharger_en_excel'),
    path('tableau_modules', views.tableau_module, name='tableau_modules'),
    path('dictionnaire', views.tableau_dictionnaire, name='dictionnaire'),
    path('exporter_en_excel', views.exporter_en_excel, name='exporter_en_excel'),
    path('recherchemotga', views.recherche_mot_programme_GA, name='recherchemotga'),
    path('ressappli', views.ajout_ressource_application, name='ressappli'),
    path('pagerechressapp',views.filtre_ressource_appli, name = "pagerechressapp"),
    path('fonctionrechressapp',views.filtre_ressource_appli, name = "fonctionrechressapp"),
    path('RessAppExtraction', views.ExtractionRessApp, name='RessAppExtraction'),
    path('CopieSupprime/<int:id>', views.CopierSupprimer, name='CopieSupprime'),
    path('tableau_ressource_off', views.recup_ressource_off, name='tableau_ressource_off'),
    path('voir_pdf/<int:id>/', views.generer_formulaire_pdf, name='voir_pdf'),
    path('recherche_par_mot/', views.recherche_par_mot, name='recherche_par_mot'),
    path('UpdateRessource/<int:id>',views.update_ressource, name = "UpdateRessource"), 
    path('UpdateApplication/<int:id>',views.update_application, name = "UpdateApplication"),
    path('',views.user_login, name = "connexion"),
    path('logout', views.user_logout, name='logout'),
    path('compte/', views.user_profile, name='compte'),
    path('changer-mot-de-passe/', PasswordChangeView.as_view(), name='password_change'),
    path('changer-mot-de-passe/termine/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('Diagramme', views.example_diagramme, name='Diagramme'),
    path('diagram_metier', views.DiagramMetier, name='diagram_metier'),
    path('diagram_filiale', views.DiagramFiliale, name='diagram_filiale'),
    path('MajDonnee', views.MAJ, name='MajDonnee'),
    path('TotalDiagrammes', views.LesDiagrammes, name='TotalDiagrammes'),
    
          
]
