from django.contrib import admin
from .models import Domaine
from .models import Programme, Profil, Droit, Habilitation, Ressource, Application, RessourceApplication

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_domaine')

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_programme', 'description_programme', 'domaine_programme')
    
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_profil', 'description_profil')

@admin.register(Droit)
class DroitAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle_droit', 'symbole_droit')

@admin.register(Habilitation)
class HabilitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'profil', 'domaine','programme', 'droit' )    
     

@admin.register(Ressource)
class RessourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom','email', 'matricule', 'numero_ip', 'departement', 'service', 'statut', 'manager', 'date_debut', 'date_fin' ) 


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'application', 'description')   


@admin.register(RessourceApplication)
class RessourceApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ressource', 'application')       

    