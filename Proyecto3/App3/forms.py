from django import forms

class JugadorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField() #Porque son letras

class ClubFormulario(forms.Form):
    equipo = forms.CharField() #Porque son letras

class DorsalFormulario(forms.Form):
    dorsal = forms.IntegerField() # porque son numeros

class BuscarJugadorForm(forms.Form):
    jugador = forms.CharField() 





