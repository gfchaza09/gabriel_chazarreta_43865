from django.shortcuts import render

from .models import Videojuego, Consola, Accesorio
from .forms import VideojuegoForm, ConsolaForm, AccesorioForm, BusquedaForm

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    form = VideojuegoForm()

    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'tercera_preentrega_app/lista_videojuegos.html', {'videojuegos': videojuegos, 'form': form})

def detalle_videojuego(request, pk):
    videojuego = Videojuego.objects.get(pk=pk)
    return render(request, 'tercera_preentrega_app/detalle_videojuego.html', {'videojuego': videojuego})

def lista_consolas(request):
    consolas = Consola.objects.all()
    form = ConsolaForm()

    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tercera_preentrega_app/lista_consolas.html', {'consolas': consolas, 'form': form})

def detalle_consola(request, pk):
    consola = Consola.objects.get(pk=pk)
    return render(request, 'tercera_preentrega_app/detalle_consola.html', {'consola': consola})

def lista_accesorios(request):
    accesorios = Accesorio.objects.all()
    form = AccesorioForm()

    if request.method == 'POST':
        form = AccesorioForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tercera_preentrega_app/lista_accesorios.html', {'accesorios': accesorios, 'form': form})

def detalle_accesorio(request, pk):
    accesorio = Accesorio.objects.get(pk=pk)
    return render(request, 'tercera_preentrega_app/detalle_accesorio.html', {'accesorio': accesorio})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            tipo_busqueda = form.cleaned_data['tipo_busqueda']

            if tipo_busqueda == 'videojuego':
                resultados = Videojuego.objects.filter(titulo__icontains=termino_busqueda)
            elif tipo_busqueda == 'consola':
                resultados = Consola.objects.filter(nombre__icontains=termino_busqueda)
            else:
                resultados = Accesorio.objects.filter(nombre__icontains=termino_busqueda)

            return render(request, 'tercera_preentrega_app/resultados_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda})

    else:
        form = BusquedaForm()

    return render(request, 'tercera_preentrega_app/buscar.html', {'form': form})