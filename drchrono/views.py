# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout as drchrono_logout


def user(request):
    template = 'user.html'
    context = { 'username': request.user}
    return render(request, template, context)

def logout(request):
    drchrono_logout(request)
    return redirect('/')