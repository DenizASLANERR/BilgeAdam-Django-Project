from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Kullanıcı Adı',
        min_length=3,
        max_length=30,
        error_messages = {'required': 'Kullanıcı Adı zorunludur'},
        widget = forms.TextInput(attrs={'placeholder': 'Kullanıcı adınızı giriniz'})
    )

    first_name = forms.CharField(
        label='Ad',
        min_length=3,
        max_length=30,
        error_messages={'required': 'Adınız zorunludur'},
        widget = forms.TextInput(attrs={'placeholder': 'Adınızı giriniz'})
    )

    last_name = forms.CharField(
        label='Soyad',
        min_length=3,
        max_length=30,
        error_messages={'required': 'Soyadınız zorunludur'},
        widget = forms.TextInput(attrs={'placeholder': ' Soyadınızı giriniz'})
    )

    email = forms.EmailField(
        label="Email",
        min_length=3,
        max_length=50,
        error_messages={'required': 'E-mail zorunludur'},
        widget = forms.TextInput(attrs={'placeholder': 'E-mail giriniz'})
    )

    password = forms.CharField(
        label='Şifre',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi giriniz'}),
        error_messages={'required': 'Parola zorunludur'},
    )

    confirm = forms.CharField(
        label='Şifre Onayı',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi onaylayın'}),
        error_messages={'required': 'Parola onayı zorunludur'}
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Aynı Değil!")

        values = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        return values


    class Meta:
        model = User
        fields = ('username', 'first_name', "last_name", 'email', 'password', 'confirm')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Kullanıcı adı',
        widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adınızı giriniz'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi giriniz'})
    )
