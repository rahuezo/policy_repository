# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from polrep.models import Policy, MunicipalityName, Subtype, MunicipalityType

import os
import re


@login_required(login_url='/login')
def configuration_view(request):
    fn, ln = (request.user.first_name, request.user.last_name)
    username = request.user.username

    current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username

    superuser = request.user.is_superuser

    available_folders = os.listdir(settings.MEDIA_ROOT)
    subtypes = ', '.join([st.subtype_name.strip() for st in Subtype.objects.all()])
    muni_types = ', '.join([mt.mtype.strip() for mt in MunicipalityType.objects.all()])

    if request.user.username:
        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'subtypes': subtypes,
            'muni_types': muni_types,
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


def prepare_file_for_searching(folder, file_name):
    new_folder = folder.replace(' ', '_')
    new_file_name = ' '.join(file_name.lower().split()).replace(' ', '_')

    return "{0}-{1}".format(new_folder, new_file_name), ' '.join(re.findall(r'of (.*?) [0-9]+', file_name))


@login_required(login_url='/login')
def add_policy_subtype_view(request):
    fn, ln = (request.user.first_name, request.user.last_name)
    username = request.user.username
    current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username
    superuser = request.user.is_superuser
    available_folders = os.listdir(settings.MEDIA_ROOT)

    subtypes = ', '.join([st.subtype_name.strip() for st in Subtype.objects.all()])
    muni_types = ', '.join([mt.mtype.strip() for mt in MunicipalityType.objects.all()])

    if request.method == 'POST':

        new_policy_subtype = request.POST.get('new-policy-subtype')

        new_policy_subtype_object = Subtype(subtype_name=new_policy_subtype.strip())
        new_policy_subtype_object.save()

        subtypes = ', '.join([st.subtype_name.strip() for st in Subtype.objects.all()])
        muni_types = ', '.join([mt.mtype.strip() for mt in MunicipalityType.objects.all()])

        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'subtypes': subtypes,
            'muni_types': muni_types,
        }

    else:
        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'subtypes': subtypes,
            'muni_types': muni_types,
        }
    return render(request, 'configuration/configuration.html', context)


@login_required(login_url='/login')
def add_muni_type_view(request):
    fn, ln = (request.user.first_name, request.user.last_name)
    username = request.user.username
    current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username
    superuser = request.user.is_superuser
    available_folders = os.listdir(settings.MEDIA_ROOT)

    subtypes = ', '.join([st.subtype_name.strip() for st in Subtype.objects.all()])
    muni_types = ', '.join([mt.mtype.strip() for mt in MunicipalityType.objects.all()])

    if request.method == 'POST':

        new_muni_type = request.POST.get('new-municipality-type')

        new_muni_type_object = MunicipalityType(mtype=new_muni_type.strip())
        new_muni_type_object.save()

        subtypes = ', '.join([st.subtype_name.strip() for st in Subtype.objects.all()])
        muni_types = ', '.join([mt.mtype.strip() for mt in MunicipalityType.objects.all()])

        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'subtypes': subtypes,
            'muni_types': muni_types,
        }

    else:
        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'subtypes': subtypes,
            'muni_types': muni_types,
        }
    return render(request, 'configuration/configuration.html', context)


@login_required(login_url='/login')
def upload_files_to_library_view(request):
    fn, ln = (request.user.first_name, request.user.last_name)
    username = request.user.username
    current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username
    superuser = request.user.is_superuser
    available_folders = os.listdir(settings.MEDIA_ROOT)

    if request.method == 'POST' and request.FILES.getlist('policy-files'):
        policy_files = request.FILES.getlist('policy-files')
        folder_to_store = request.POST.get('pol-subtype-select')

        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, folder_to_store))

        uploaded_files = []

        for pf in policy_files:
            file_name = fs.save(pf.name, pf)
            fpath = prepare_file_for_searching(folder_to_store, pf.name)
            muni_name = fpath[1]

            policy_object = Policy(file_path=fpath[0])
            policy_object.save()

            mun_name_object = MunicipalityName(name=muni_name)
            mun_name_object.save()

            uploaded_files.append(file_name)

        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
            'uploaded_files': uploaded_files,
        }

    else:
        context = {
            'current_user': current_user,
            'current_user_email': request.user.email,
            'first_name': fn,
            'last_name': ln,
            'super_user': superuser,
            'available_folders': available_folders,
        }

    return render(request, 'configuration/configuration.html', context)
