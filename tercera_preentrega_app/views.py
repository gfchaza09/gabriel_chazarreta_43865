from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Videojuego, Consola, Accesorio, Review
from .forms import VideojuegoForm, ConsolaForm, AccesorioForm, BusquedaForm, ReviewForm, UserRegisterForm, EditarPerfilForm, LoginForm

def user_not_logged_in(user):
    return not user.is_authenticated

@login_required
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    form = VideojuegoForm()

    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tercera_preentrega_app:lista_videojuegos')


    return render(request, 'tercera_preentrega_app/lista_videojuegos.html', {'videojuegos': videojuegos, 'form': form})

@login_required
def detalle_videojuego(request, pk):
    videojuego = Videojuego.objects.get(pk=pk)
    review_form = ReviewForm()
    reviews = Review.objects.filter(videojuego=videojuego)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.usuario = request.user
            review.videojuego = videojuego
            review.save()
            return redirect('tercera_preentrega_app:detalle_videojuego', pk=pk)
        
    return render(request, 'tercera_preentrega_app/detalle_videojuego.html', {'videojuego': videojuego, 'reviews': reviews, 'review_form': review_form})

@login_required
def editar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)

    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('/videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)

    return render(request, 'tercera_preentrega_app/editar_videojuego.html', {'form': form})

@login_required
def eliminar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)

    if request.method == 'POST':
        videojuego.delete()
        return redirect('/videojuegos')

    return render(request, 'tercera_preentrega_app/eliminar_videojuego.html', {'videojuego': videojuego})

@login_required
def lista_consolas(request):
    consolas = Consola.objects.all()
    form = ConsolaForm()

    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tercera_preentrega_app:lista_consolas')

    return render(request, 'tercera_preentrega_app/lista_consolas.html', {'consolas': consolas, 'form': form})

@login_required
def detalle_consola(request, pk):
    consola = Consola.objects.get(pk=pk)
    review_form = ReviewForm()
    reviews = Review.objects.filter(consola=consola)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.usuario = request.user
            review.consola = consola
            review.save()
            return redirect('tercera_preentrega_app:detalle_consola', pk=pk)
        
    return render(request, 'tercera_preentrega_app/detalle_consola.html', {'consola': consola, 'reviews': reviews, 'review_form': review_form})

@login_required
def editar_consola(request, pk):
    consola = get_object_or_404(Consola, pk=pk)

    if request.method == 'POST':
        form = ConsolaForm(request.POST, instance=consola)
        if form.is_valid():
            form.save()
            return redirect('/consolas')
    else:
        form = ConsolaForm(instance=consola)

    return render(request, 'tercera_preentrega_app/editar_consola.html', {'form': form})

@login_required
def eliminar_consola(request, pk):
    consola = get_object_or_404(Consola, pk=pk)

    if request.method == 'POST':
        consola.delete()
        return redirect('/consolas')

    return render(request, 'tercera_preentrega_app/eliminar_consola.html', {'consola': consola})

@login_required
def lista_accesorios(request):
    accesorios = Accesorio.objects.all()
    form = AccesorioForm()

    if request.method == 'POST':
        form = AccesorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tercera_preentrega_app:lista_accesorios')

    return render(request, 'tercera_preentrega_app/lista_accesorios.html', {'accesorios': accesorios, 'form': form})

@login_required
def detalle_accesorio(request, pk):
    accesorio = Accesorio.objects.get(pk=pk)
    review_form = ReviewForm()
    reviews = Review.objects.filter(accesorio=accesorio)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.usuario = request.user
            review.accesorio = accesorio
            review.save()
            return redirect('tercera_preentrega_app:detalle_accesorio', pk=pk)
        
    return render(request, 'tercera_preentrega_app/detalle_accesorio.html', {'accesorio': accesorio, 'reviews': reviews, 'review_form': review_form})

@login_required
def editar_accesorio(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)

    if request.method == 'POST':
        form = AccesorioForm(request.POST, instance=accesorio)
        if form.is_valid():
            form.save()
            return redirect('/accesorios')
    else:
        form = AccesorioForm(instance=accesorio)

    return render(request, 'tercera_preentrega_app/editar_accesorio.html', {'form': form})

@login_required
def eliminar_accesorio(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)

    if request.method == 'POST':
        accesorio.delete()
        return redirect('/accesorios')

    return render(request, 'tercera_preentrega_app/eliminar_accesorio.html', {'accesorio': accesorio})

@login_required
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

            return render(request, 'tercera_preentrega_app/resultados_busqueda.html', {'resultados': resultados, 'tipo_busqueda': tipo_busqueda, 'termino_busqueda': termino_busqueda})

    else:
        form = BusquedaForm()

    return render(request, 'tercera_preentrega_app/buscar.html', {'form': form})

@user_passes_test(user_not_logged_in, login_url='tercera_preentrega_app:lista_videojuegos')
def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return redirect('/perfil')
        
    form = LoginForm()

    return render(request, 'tercera_preentrega_app/login.html', {'form':form})

@user_passes_test(user_not_logged_in, login_url='tercera_preentrega_app:lista_videojuegos')
def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return redirect('/', {"mensaje": "Usuario Creado, Bienvenido/a "+ username})
        
    else:
        form = UserRegisterForm()

    return render(request, 'tercera_preentrega_app/registro.html', {"form": form})

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'tercera_preentrega_app/perfil.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            form.save()
            return redirect('/perfil')
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'tercera_preentrega_app/editar_perfil.html', {'usuario': usuario, 'form': form})

def acerca_de(request):
    return render(request, 'tercera_preentrega_app/acerca_de.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)