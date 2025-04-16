# from django.http import HttpResponse
from django.shortcuts import render



def start(request):
    return render(request, 'index.html')

def apointment(request):
    return render(request, 'starter-page.html')    