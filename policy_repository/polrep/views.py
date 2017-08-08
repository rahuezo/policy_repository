# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import MunicipalityName, MunicipalityType, Year, Subtype, PolicyStance, Policy

from django.http import HttpResponse
from django.conf import settings

import os


def index(request):
    subtypes = Subtype.objects.all()
    muni_names = MunicipalityName.objects.all()
    muni_types = MunicipalityType.objects.all()
    years = Year.objects.all()
    stances = PolicyStance.objects.all()

    try:
        fn, ln = (request.user.first_name, request.user.last_name)
        username = request.user.username

        current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username

        context = {
            'current_user': current_user,
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
        }

    except:
        context = {
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
        }

    return render(request, 'polrep/index.html', context)


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
        if fetched_file is not False:
            results.append(fetched_file)

    subtypes = Subtype.objects.all()
    muni_names = MunicipalityName.objects.all()
    muni_types = MunicipalityType.objects.all()
    years = Year.objects.all()
    stances = PolicyStance.objects.all()

    try:
        fn, ln = (request.user.first_name, request.user.last_name)
        username = request.user.username

        current_user = "{0} {1}".format(fn, ln) if len(fn) > 0 and len(ln) > 0 else username

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
            'current_user': current_user,
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
        }

    except:
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
            'subtypes': subtypes,
            'muni_names': muni_names,
            'muni_types': muni_types,
            'years': years,
            'stances': stances,
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
