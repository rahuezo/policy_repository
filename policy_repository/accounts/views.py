# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from polrep.models import MunicipalityName, MunicipalityType, Year, Subtype, PolicyStance, Policy


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        login(request, user)

        # Redirect User Here

        subtypes = Subtype.objects.all()
        muni_names = MunicipalityName.objects.all()
        muni_types = MunicipalityType.objects.all()
        years = Year.objects.all()
        stances = PolicyStance.objects.all()

        context = {
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
            'current_user': user.username,
        }
        return render(request, "polrep/index.html", context)


    context = {
        "form": form
    }
    return render(request, "accounts/signin.html", context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")

        user.set_password(password)

        user.save()
        login(request, user)

        # Redirect here

        subtypes = Subtype.objects.all()
        muni_names = MunicipalityName.objects.all()
        muni_types = MunicipalityType.objects.all()
        years = Year.objects.all()
        stances = PolicyStance.objects.all()

        context = {
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
            'current_user': user.username,
        }
        return render(request, "polrep/index.html", context)

    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


def logout_view(request):
    logout(request)

    subtypes = Subtype.objects.all()
    muni_names = MunicipalityName.objects.all()
    muni_types = MunicipalityType.objects.all()
    years = Year.objects.all()
    stances = PolicyStance.objects.all()

    context = {
        'subtypes': subtypes,
        'muni_names': muni_names,
        'muni_types': muni_types,
        'years': years,
        'stances': stances,
        'logout_message': "You have successfully logged out!",
    }
    return render(request, "polrep/index.html", context)

