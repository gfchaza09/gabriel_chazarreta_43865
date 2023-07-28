from django import forms
from .models import Videojuego, Consola, Accesorio

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'desarrollador', 'genero', 'año_lanzamiento']

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre', 'fabricante', 'año_lanzamiento']

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['nombre', 'tipo']

class BusquedaForm(forms.Form):
    OPCIONES_BUSQUEDA = [
        ('videojuego', 'Videojuego'),
        ('consola', 'Consola'),
        ('accesorio', 'Accesorio'),
    ]

    termino_busqueda = forms.CharField(label='Buscar', max_length=100)
    tipo_busqueda = forms.ChoiceField(label='Tipo de búsqueda', choices=OPCIONES_BUSQUEDA)