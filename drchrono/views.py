# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout as drchrono_logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail,send_mass_mail
from .models import PatientModel
from .forms import birthdayEmailForm
from django.conf import settings
import requests
from pprint import pprint

def home(request):
    if not request.user.is_authenticated():
        return redirect('/')

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
    #get all patients who have an email id and birthdate
    message = settings.EMAIL_BIRTHDAY_DEFAULT_MESSAGE
    p = PatientModel.objects.exclude(patient_email="").exclude(birthday=None)
    form = birthdayEmailForm(request.POST or None, initial={'message': message})
    confirmation = None

    if form.is_valid():
        name = "drchrono team"
        subject = "Happy Birthday from drchrono!"
        message = form.cleaned_data['message']
        from_email = "drchrono@drchrono.com"
        recipient_list = ["kashyapbhansali7@gmail.com","sagarshah2007@gmail.com"]
        #datatuple for sending mass mail
        email_tuple = ((subject, message, from_email, recipient_list),)
        count = send_mass_mail(email_tuple, fail_silently=False)
        confirmation = "Birthday wishes were sent to %s people." % count

    template = 'user.html'
    context = {'patient_data': p, 'form': form, 'confirmation':confirmation}


    return render(request, template, context)

def logout(request):
    drchrono_logout(request)
    return redirect('/')