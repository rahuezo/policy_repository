# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login')
def configuration_view(request):
    fn, ln = (request.user.first_name, request.user.last_name)
    username = request.user.username

    current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username

    superuser = request.user.is_superuser

    if request.user.username:
        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
        }

    return render(request, "configuration/configuration.html", context)


@login_required(login_url='/login')
def update_people_view(request):
    current_user = request.user.username

    new_first_name = request.POST.get('first_name')
    new_last_name = request.POST.get('last_name')
    new_email = request.POST.get('email')

    user_config = User.objects.get(username=current_user)

    if new_first_name != user_config.first_name:
        user_config.first_name = new_first_name

    if new_last_name != user_config.last_name:
        user_config.last_name = new_last_name

    if new_email != user_config.email:
        user_config.email = new_email

    user_config.save()

    current_user = "{0} {1}".format(user_config.first_name, user_config.last_name)
    superuser = request.user.is_superuser

    context = {
        'current_user': current_user,
        'current_user_email': user_config.email,
        'first_name': user_config.first_name,
        'last_name': user_config.last_name,
        'applied_update': True,
        'super_user': superuser,
    }

    return render(request, 'configuration/configuration.html', context)
