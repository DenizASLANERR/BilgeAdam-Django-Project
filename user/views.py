from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        newUser = User(username=username, first_name=first_name, last_name=last_name, email=email)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)

        return redirect("pages:index")

    context = {
        'form': form,
    }
    return render(request, "registration/register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        'form': form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("pages:index")
        else:
            context['error'] = "Geçersiz kullanıcı adı veya şifre."

    return render(request, "registration/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("pages:index")
