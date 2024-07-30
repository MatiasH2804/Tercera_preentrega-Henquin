from django.shortcuts import render
from App3.models import Jugador, Club, Dorsal
from App3.forms import JugadorFormulario, ClubFormulario, DorsalFormulario, BuscarJugadorForm
# Create your views here.
def inicio(request):
    return render(request, "App3/index.html")

def jugador(request):
    if request.method == "POST":
        mi_formulario = JugadorFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Jugador(nombre=informacion["nombre"], apellido=informacion["apellido"])
            curso.save()

            return render(request, "App3/index.html")
    else:
        mi_formulario = JugadorFormulario()

    return render(request, "App3/jugador.html", {"mi_formulario": mi_formulario})

def club(request):
    if request.method == "POST":
        mi_formulario = ClubFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Club(equipo=informacion["equipo"])
            curso.save()

            return render(request, "App3/index.html")
    else:
        mi_formulario = ClubFormulario()

    return render(request, "App3/club.html", {"mi_formulario": mi_formulario})

def dorsal(request):
    if request.method == "POST":
        mi_formulario = DorsalFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Dorsal(dorsal=informacion["dorsal"])
            curso.save()

            return render(request, "App3/index.html")
    else:
        mi_formulario = DorsalFormulario()

    return render(request, "App3/dorsal.html", {"mi_formulario": mi_formulario})

def buscar_jugador(request):
    if request.method == "POST":
        mi_formulario = BuscarJugadorForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            nombres = Jugador.objects.filter(nombre__icontains=informacion["jugador"])

            return render(request, "App3/mostrar_jugadores.html", {"nombres": nombres})
    else:
        mi_formulario = BuscarJugadorForm()

    return render(request, "App3/buscar-jugador.html", {"mi_formulario": mi_formulario})