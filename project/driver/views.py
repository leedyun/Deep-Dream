# driver/views.py
from django.shortcuts import render

def articles_home(request):
    return render(request, 'driver/home.html')
