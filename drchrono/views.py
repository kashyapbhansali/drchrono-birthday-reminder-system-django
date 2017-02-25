# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout as drchrono_logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PatientModel
import requests
from pprint import pprint

def home(request):
    template = 'home.html'
    context = {'username': request.user}
    user_instance = request.user.social_auth.get()
    access_token = user_instance.extra_data['access_token']
    #print access_token
    headers = {
        'Authorization': 'Bearer %s' % access_token,
    }

    # this endpoint returns a few lists of patients at a time
    # it has next and previous points to indicate if more patients are available
    patients_url = 'https://drchrono.com/api/patients'
    patient_list = []

    while True:
        r = requests.get(patients_url, headers=headers)
        print r.raise_for_status()
        patient_data = r.json()
        #pprint(patient_data)
        patient_list.extend(patient_data['results'])
        if not patient_data['next']:
            break

    #save data using PatientModel

    for patient in patient_list:
        p = PatientModel(
            first_name=patient['first_name'],
            last_name=patient['last_name'],
            doctor_id=patient['doctor'],
            gender=patient['gender'],
            birthday=patient['date_of_birth'],
            patient_id=patient['id'],
            patient_email=patient['email']
        )
        p.save()

    return render(request, template, context)

def user(request):
    p = PatientModel.objects.exclude(patient_email="").exclude(birthday=None)
    #print p
    template = 'user.html'
    context = {'patient_data': p}
    return render(request, template, context)

def logout(request):
    drchrono_logout(request)
    return redirect('/')