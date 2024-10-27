from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')

    def clean(self):
        cleaned_data = super().clean()
        password1=cleaned_data.get('password1')
        password2=cleaned_data.get('password2')
        if not password1 == password2:
            self.add_error('password2', "Please enter same password")
        return cleaned_data

class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label="Password", widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username', 'password')

    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid credentials")
            
class ItemPreferencesForm(forms.Form):
    vegetarian = forms.BooleanField(label="Vegetarian", required=False)
    vegan = forms.BooleanField(label="Vegan", required=False)
    glutenFree = forms.BooleanField(label="Gluten Free", required=False)
    dairy = forms.BooleanField(label="Milk", required=False)
    peanuts = forms.BooleanField(label="Peanut",required=False)
    soybean = forms.BooleanField(label="Soybean",required=False)
    wheat = forms.BooleanField(label="Wheat", required=False)
    eggs = forms.BooleanField(label="Eggs", required=False)
    coconut = forms.BooleanField(label="Coconut", required=False)
    fish = forms.BooleanField(label="Fish", required=False)
    shellfish = forms.BooleanField(label="Shellfish", required=False)
    sesame = forms.BooleanField(label="Sesame", required=False)

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('vegetarian','vegan','glutenFree','dairy','peanuts','soybean','wheat','eggs','coconut','fish','shellfish','sesame')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data