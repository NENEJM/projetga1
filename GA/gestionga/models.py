from django.db import models
from django.utils import formats
from django.urls import reverse

class Domaine(models.Model):               #Modele Domaine
    nom_domaine = models.CharField(max_length=70) 
    def __str__(self):
        return f"{self.nom_domaine}"


class Programme(models.Model):                             #Modele programme
    nom_programme = models.CharField(max_length=100) 
    description_programme = models.CharField(max_length=100)
    domaine_programme = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name='programme_domaine')

    def __str__(self):
         return f"{self.nom_programme} "



class Profil(models.Model):
    nom_profil = models.CharField(max_length=100)
    description_profil = models.TextField() 

    def __str__(self):
        return f"{self.nom_profil}"

class Droit(models.Model):
    libelle_droit = models.CharField(max_length=100)
    symbole_droit = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.symbole_droit}"         


class Habilitation(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='habilitations')
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='habilitations')
    droit = models.ForeignKey(Droit, on_delete=models.CASCADE, related_name='habilitations')
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name='habilitations')

    def __str__(self):
        return f"Habilitation {self.profil} - {self.programme} - {self.droit}"
    


##################### RESSOURCE MODELE #############################

DEPARTEMENT_CHOICES = (
    ('GA1', 'GA 1'),
    ('GA2', 'GA 2'),
)

MANAGER_CHOICES = (
    ('Douanla Fleurette', 'Douanla Fleurette'),
    ('Koffi Katche', 'Koffi Katche'),
)

SERVICE_CHOICES = (
    ('GDD', 'GDD'),
    ('REFERENTIEL', 'REFERENTIEL'),
    ('ENGAGEMENT', 'ENGAGEMENT'),
    ('CANAUX_ET_CONFORMITE', 'CANAUX ET CONFORMITE'),
    ('MONETIQUE', 'MONETIQUE'),
    ('CASH_MANAGEMENT', 'CASH MANAGEMENT'),
)

STATUT_CHOICES = (
    ('Interne', 'Interne'),
    ('Externe', 'Externe'),
    ('Stagiaire', 'Stagiaire'),
)

MANAGERS_CHOICES = [
        ('KOFFI KATCHE OLIVIER', 'KOFFI KATCHE OLIVIER'),
        ('DOUANLA FLEURETTE', 'DOUANLA FLEURETTE'),
    ]

class Ressource(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True,)
    matricule = models.CharField(max_length=20, unique=True,)
    numero_ip = models.CharField(max_length=4, blank=True, null=True)
    departement = models.CharField(max_length=10, choices=DEPARTEMENT_CHOICES)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    manager = models.CharField(max_length=20, choices=MANAGERS_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.email}"

    def get_absolute_url(self):
        return reverse('remplir_pdf', args=[str(self.id)])


################ Modele Application #########################################

class Application(models.Model):               
    application = models.CharField(max_length=70) 
    description = models.TextField()

    def __str__(self):
        return f"{self.application}"  


####################### MODELE PROFIL GA ######################################
                       
 #Modele DICTIONNAIRE

class Dictionnaire(models.Model):                             
    module = models.CharField(max_length=100) 
    programme = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    typ = models.CharField(max_length=100)      
    def __str__(self):
         return f"{self.programme} "

####### Modele Programme SGCI ########################

class Sgci(models.Model):
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "
    
####### Modele Programme SGSN ########################

class Sgsn(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "  
     
####### Modele Programme SGBE ########################

class Sgbe(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "       
    

####### Modele Programme SGTG ########################

class Sgtg(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "   
    

####### Modele Programme SGBF ########################

class Sgbf(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      
    


####### Modele Programme SGCONGO ########################

class Sgcongo(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      
    


####### Modele Programme SGCAM ########################

class Sgcam(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      
    

####### Modele Programme SGM ########################

class Sgm(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "     



############ TABLE MODULE ##########################

class Table_Module(models.Model):
    nom_module = models.CharField(max_length=70)
    description_module = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom_module}" 
    
################### APPLICATION PAR RESSOURCE ###################

class RessourceApplication(models.Model):
    ressource = models.ForeignKey('Ressource', on_delete=models.CASCADE)
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ressource.prenom} {self.ressource.nom} - {self.application.application}"

    class Meta:
        unique_together = ('ressource', 'application')


################## RESSOURCE OFF ########################

class RessourceOff(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    matricule = models.CharField(max_length=20)
    numero_ip = models.CharField(max_length=4, blank=True, null=True)
    departement = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    statut = models.CharField(max_length=100)
    manager = models.CharField(max_length=20, choices=MANAGERS_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    date_desactivation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.date_desactivation}"



################ MODELE RESULTAT RECHERCHE POUR RECHERCHE PAR MOT ###############

from django.db import models

class ResultatRecherche(models.Model):
    module = models.TextField()
    programme_filiale = models.TextField()
    intitule = models.TextField()
    cmis = models.TextField()

    def __str__(self):
        return f"{self.module} - {self.programme_filiale} - {self.intitule} - {self.cmis}"




#################### PROGRAMME FILIALE EXPLOIT #########################################

####### Modele Programme SGCI ########################

class SgciX(models.Model):
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "
    
####### Modele Programme SGSN ########################

class SgsnX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "  
     
####### Modele Programme SGBE ########################

class SgbeX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "       
    

####### Modele Programme SGTG ########################

class SgtgX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "   
    

####### Modele Programme SGBF ########################

class SgbfX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      
    


####### Modele Programme SGCONGO ########################

class SgcongoX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      
    


####### Modele Programme SGCAM ########################

class SgcamX(models.Model):                             
    module = models.CharField(max_length=100)                             
    programme_filiale = models.CharField(max_length=100) 
    intitule = models.CharField(max_length=100)
    cmis = models.CharField(max_length=100)                   
    def __str__(self):
         return f"{self.programme_filiale} "      