from django import forms
from .models import Articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]