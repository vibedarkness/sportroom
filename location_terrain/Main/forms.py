from django import forms
from django.forms.widgets import DateInput, TextInput

from .models import *

from django.core.validators import RegexValidator
from .models import Gerant

# Gestion du lowercase


class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# Gestion du Uppercase


class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class GerantForm(forms.ModelForm):

    # validations
    firstname = forms.CharField(label='Prenom', min_length=3, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Prenom','style': 'text-transform: capitalize'}))


    lastname = forms.CharField(label='Nom', min_length=2, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Nom', 'style': 'text-transform: capitalize'}))

    username = forms.CharField(label="Nom d'utlisateur", min_length=2, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': "Nom d'utlisateur", 'style': 'text-transform: capitalize'}))


    address = forms.CharField(label='Adresse', min_length=1, max_length=3, validators=[RegexValidator(
        message='ce champ ne dois contenir que des entiers et caracteres')], widget=forms.TextInput(attrs={'placeholder': 'Adresse'}))


    telephone = forms.CharField(label='Telephone', min_length=1, max_length=3, validators=[RegexValidator(
        message='ce champ ne dois contenir que des entiers et caracteres')], widget=forms.TextInput(attrs={'placeholder': 'Telephone'}))



    email = Lowercase(label='Email', min_length=5, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="ceci n'est pas un email valide")], widget=forms.TextInput(attrs={'placeholder': 'Email','style':'font-size:13px'}))
    # phone = forms.CharField(label='Telephone' ,min_length=1, max_length=3, validators=[RegexValidator(r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs= {'placeholder':'Telephone'}))


    # fichier=forms.FileField(label='Entrez votre cv', widget=forms.ClearableFileInput(attrs={'style':'font-size:13px'}))


    # GENRE=[('M','Masculin'),('F','Feminin')]
    # genre=forms.CharField(label='Genre',widget=forms.RadioSelect(choices=GENRE))

    class Meta:
        model = Gerant
        # fields = ['firstname', 'lastname','job', 'email', 'age', 'phone', 'message']
        exclude = ['created_at', 'updated_at']

        

    # super fonction
    # def init(self, *args, **kwargs):
    #     super(CandidatForm, self).init(*args, **kwargs)

# control panel
        # input required


        # input desactivé
        # self.fields["firstname"].disabled=True

        # input readonly
        # self.fields["email"].widget.attrs.update({'readonly':'readonly'})

        # readonly for full input(meme chose pour disabled(desactivé))

        # readonly=["firstname","lastname","age","email","phone","message"]

        # for readvibe in readonly:
        #     self.fields[readvibe].widget.attrs['readonly']='true'

        # select option
        # self.fields["personnality"].choices = [
        #     ('', 'Choisissez votre personnalité'), ] + list(self.fields["personnality"].choices)[1:]

