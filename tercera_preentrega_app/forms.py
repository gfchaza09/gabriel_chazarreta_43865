from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Videojuego, Consola, Accesorio, Perfil, Review

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['calificacion', 'comentario']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    avatar = forms.ImageField(required=False)

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

    def save(self, commit=True):
        user = super().save(commit=False)

        if 'avatar' in self.cleaned_data and self.cleaned_data['avatar']:
            user.save()
            perfil = Perfil(user=user, avatar=self.cleaned_data['avatar'])
            perfil.save()
    
        if commit:
            user.save()
        
        return user
    
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar']
    
    avatar = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Opcional: quitar el mensaje de ayuda

    def save(self, commit=True):
        user = super().save(commit=False)

        if 'avatar' in self.cleaned_data and self.cleaned_data['avatar']:
            perfil, created = Perfil.objects.get_or_create(user=user)
            perfil.avatar = self.cleaned_data['avatar']
            perfil.save()

        if commit:
            user.save()
        
        return user