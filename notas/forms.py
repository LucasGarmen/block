# notas/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: MiUsuario123'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo 8 caracteres'})
    )
    password2 = forms.CharField(
        label='Repetir contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetí la contraseña'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tuemail@email.com'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
