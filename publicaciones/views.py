from django.shortcuts import render
from .models import publication

# Create your views here.

def about(request):
    publications = publication.objects.all()
    return render(request, "publicaciones/about.html", {'publications': publications})