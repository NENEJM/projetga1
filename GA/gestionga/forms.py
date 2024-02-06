from django.core import validators
from django import forms
from .models import Domaine
from .models import Programme
from .models import Profil, Droit, Habilitation, Ressource, Application, Dictionnaire, Sgci, Sgsn
from .models import Table_Module, RessourceApplication, ResultatRecherche
from django.contrib.auth.forms import AuthenticationForm

####################  FORMULAIRE DOMAINE #################  

class Form_domaine(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = ['nom_domaine'] 
        widgets = {
              'nom_domaine': forms.TextInput(attrs={'class': 'form-control'}),

        }

####################  FORMULAIRE PROGRAMME ################# 

class Form_programme(forms.ModelForm):
    
    class Meta:
        model = Programme
        fields = ['nom_programme', 'description_programme', 'domaine_programme']

    widgets = {
        'nom_programme': forms.TextInput(attrs={'class': 'form-control'}),
        'description_programme': forms.TextInput(attrs={'class': 'form-control'}),
        'domaine_programme': forms.Select(attrs={'class': 'form-control'}),
       
    }

    labels = {
        'nom_programme': 'Nom du Programme',
        'description_programme': 'Description du Programme',
        'domaine_programme': 'Domaine Programme',
    }


####################  FORMULAIRE PROFIL #################

class Form_profil(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['nom_profil', 'description_profil']
        widgets = {
            'nom_profil': forms.TextInput(attrs={'class': 'form-control'}),
            'description_profil': forms.TextInput(attrs={'class': 'form-control'}),
        }

####################  FORMULAIRE DROIT #################

class Form_droit(forms.ModelForm):
    class Meta:
        model = Droit
        fields = ['libelle_droit', 'symbole_droit']
        widgets = {
            'libelle_droit': forms.TextInput(attrs={'class': 'form-control'}),
            'symbole_droit': forms.TextInput(attrs={'class': 'form-control'}),
        }

######################## FORMULAIRE HABILITATIONS ######################

class Form_habilitation(forms.ModelForm):
    class Meta:
        model = Habilitation
        fields = ['profil', 'programme', 'domaine', 'droit']

    def __init__(self, *args, **kwargs):
        super(Form_habilitation, self).__init__(*args, **kwargs)
        self.fields['programme'].queryset = Programme.objects.all()  # Pour afficher tous les programmes disponibles
        self.fields['droit'].queryset = Droit.objects.all()  # Pour afficher tous les droits disponibles



############# FORMULAIRE DE RECHERCHE PROJET ##############################


class Form_rchprogramme(forms.Form):
    profil = forms.ModelChoiceField(
        queryset=Profil.objects.all(),
        empty_label="Tous les profils",
        required=False
    )

    droit = forms.ModelChoiceField(
        queryset=Droit.objects.all(),
        empty_label="Tous les droits",
        required=False
    )

    programme = forms.ModelChoiceField(
        queryset=Programme.objects.all(),
        empty_label="Tous les programmes",
        required=False
    )    

##################### PROGRAMME ABSENT #########################

class Form_ProgrammeAbsent(forms.Form):
    profil = forms.ModelChoiceField(
        queryset=Profil.objects.all(),
        empty_label="Tous les profils",
        required=False
    )

#################### RESSOURCE FORMULAIRE #########################

class Form_ressource(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = '__all__'

####################### APPLICATION ###############################

class Form_appli(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application', 'description']
        widgets = {
            'application': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


#################### FORMULAIRE DE PROFIL GA ######################

# Dans votre formulaire
class Form_ProgrammeGA(forms.Form):
    TABLE_CHOICES = [
        ('Sgci', 'Sgci'),
        ('Sgsn', 'Sgsn'),
        ('Sgbe', 'Sgbe'),
        ('Sgtg', 'Sgtg'),
        ('Sgbf', 'Sgbf'),
        ('Sgcongo', 'Sgcongo'),
        ('Sgcam', 'Sgcam'),
        ('Sgm', 'Sgm'),
    ]

    CMIS_CHOICES = [
        
        ('*', '*'),
        ('i', 'i'),
        ('C', 'C'),
        ('M', 'M'),
        ('S', 'S'),
        ('', 'Tous les CMIS'),
          
    ]

    table = forms.ChoiceField(
        choices=TABLE_CHOICES,
        label='Sélectionnez la filiale',
        required=True,
    )

    cmis = forms.ChoiceField(
        choices=CMIS_CHOICES,
        label='Sélectionnez le CMIS',
        required=False,
        initial='',
    )

    modules = forms.ModelChoiceField(
        queryset=Table_Module.objects.all(),
        empty_label="Tous les modules",
        required=False
    )


############# FORMULAIRE FICTIF TABLE MODULE ################

class Form_module(forms.ModelForm):
    class Meta:
        model = Table_Module
        fields = '__all__'    

############# FORMULAIRE FICTIF TABLE DICTIONNAIRE ################
        
class Form_Dictionnaire(forms.ModelForm):
    class Meta:
        model = Dictionnaire
        fields = '__all__' 


################# FORMULAIRE DE RECHERCHE #################

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


############ APPLICATION PAR RESSOURCE ########################

class RessourceApplicationForm(forms.ModelForm):
    class Meta:
        model = RessourceApplication
        fields = ['ressource', 'application']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ressource'].label = 'Sélectionnez la ressource'
        self.fields['application'].label = 'Sélectionnez l\'application'

    def clean(self):
        cleaned_data = super().clean()
        ressource = cleaned_data.get('ressource')
        application = cleaned_data.get('application')

        # Vérifiez si une entrée avec la même combinaison ressource et application existe déjà
        if RessourceApplication.objects.filter(ressource=ressource, application=application).exists():
            raise forms.ValidationError("Cette ressource est déjà habilitée à cette application.")

        return cleaned_data



################## FORMULAIRE FILTRE RESSOURCE APPLI ####################

class Form_filtre_ressappli(forms.Form):
    application = forms.ModelChoiceField(
        queryset=Application.objects.all(),
        empty_label="Toutes les applications",
        required=False
    )

    ressource = forms.ModelChoiceField(
        queryset=Ressource.objects.all(),
        empty_label="Toutes les ressources",
        required=False
    )



############## FORMULAIRE RECHERCHE PAR MOT ###################################

class SearchForm2(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ce tableau provient du dernier filtre'}))


###################" FORMULAIRE DE CONNEXION "######################################

class ConnexionForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Les informations d'identification fournies sont invalides. Veuillez réessayer.",
        'inactive': "Ce compte est inactif.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email', None)
        self.fields['username'].widget.attrs['placeholder'] = 'Nom utilisateur'
        self.fields['password'].widget.attrs['placeholder'] = 'Mot de passe'
