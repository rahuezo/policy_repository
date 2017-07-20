# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import MunicipalityName, MunicipalityType, Year, Subtype, PolicyStance, Policy
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import re
import os
import random


def index(request):
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
    }

    return render(request, 'polrep/index.html', context)


def register(request):

    context = {}

    return render(request, 'polrep/register.html', context)


def register_success(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if first_name is not None and last_name is not None and email is not None and password is not None:
            user_name = "{0} {1}".format(first_name, last_name)

            try:
                user_exists = User.objects.get(username=user_name)

                context = {
                    'user_exists': 'User already exists! Please re-enter your information or Sign In.'
                }

                return render(request, 'polrep/register.html', context)
            except User.DoesNotExist:
                new_user = User.objects.create_user(user_name, email, password)

                new_user.first_name = first_name
                new_user.last_name = last_name

                new_user.save()

                messages.success(request, 'Congratulations {0} {1}!<br><small>You have successfully registered your account.</small>'.format(first_name, last_name))

                # Redirect to Successful Registration page
                return HttpResponseRedirect(reverse('polrep:register_success'))
    else:
        context = {}
        return render(request, 'polrep/register.html', context)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email is not None and password is not None:
            try:
                current_user = User.objects.get(email=email)

                user_name = current_user.username

                if current_user.check_password(password) == False:
                    context = {
                        'invalid_credentials': 'The entered password does not match our records! Please try again.',
                    }

                    return render(request, 'polrep/signin.html', context)

                context = {
                    'current_user': user_name,
                    'current_user_msg': 'Welcome, {0}'.format(user_name),
                }

                return render(request, 'polrep/signin.html', context)
            except User.DoesNotExist:

                context = {
                    'invalid_credentials': 'Invalid credentials! Please try again.',
                }

                return render(request, 'polrep/signin.html', context)
    else:
        context = {}
        return render(request, 'polrep/signin.html', context)


def successful_logout(request):
    logout(request)

    return render(request, 'polrep/index.html')


def fetch_file(active_parameters, f):
    valid_fetch = all(kw in f.file_path.lower().replace('-', ' ').replace('_', ' ') for kw in active_parameters)

    if valid_fetch == True:
        return f
    else:
        return False


def get_active_parameters(parameters):
    return [str(p).lower().replace('\r\n', '') for p in parameters if p is not None]


def retrieve(request):
    query_tag_html = request.POST.get('query-tag-html')

    muni_name = request.POST.get('muni-name-select')
    muni_type = request.POST.get('muni-type-select')
    pol_stance = request.POST.get('pol-stance-select')
    pol_year = request.POST.get('pol-year-select')
    pol_subtype = request.POST.get('pol-subtype-select')

    parameters = get_active_parameters([muni_name, muni_type, pol_stance, pol_year, pol_subtype])

    all_files = Policy.objects.all()

    results = []

    for f in all_files:
        fetched_file = fetch_file(parameters, f)
        if  fetched_file is not False:
            results.append(fetched_file)

    subtypes = Subtype.objects.all()
    muni_names = MunicipalityName.objects.all()
    muni_types = MunicipalityType.objects.all()
    years = Year.objects.all()
    stances = PolicyStance.objects.all()

    context = {
        'query_tags': query_tag_html,
        'results': results,
        'number_of_results': len(results),
        'result_or_results': 'Results' if len(results) > 1 or len(results) == 0 else 'Result',
        'subtypes': subtypes,
        'muni_names': muni_names,
        'muni_types': muni_types,
        'years': years,
        'stances': stances,
        'highlights': parameters,
    }

    return render(request, 'polrep/index.html', context)


def pdf_viewer(request, pdf_name):
    pdf_name = pdf_name.replace('-', '/').replace('_', ' ')

    with open(os.path.join(settings.MEDIA_ROOT, pdf_name), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename={0}'.format(pdf_name)
        return response


def pdf_download(request, pdf_name):
    pdf_name = pdf_name.replace('-', '/').replace('_', ' ')

    with open(os.path.join(settings.MEDIA_ROOT, pdf_name), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename={0}'.format(pdf_name)
        return response
