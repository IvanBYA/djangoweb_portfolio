from django.shortcuts import render, HttpResponse
from .models import project

# Create your views here.

def home(request):
    return render(request, "portfolio/home.html")

def portfolio(request):
    projects = project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects})
