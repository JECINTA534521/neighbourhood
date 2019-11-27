from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood,Occupants,Bussiness
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']
        help_texts = {
            'username': '',
            'email': '',
            'password1':'',
            'password2':''
        }
        help_texts={'username':'','email':'','password1':'','password2':''}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Occupants
        exclude=['name']


class BussinessForm(forms.ModelForm):
    class Meta:
        model=Bussiness
        exclude = ['owner','neighborhood']

