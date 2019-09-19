from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

"""
def index(request):
	return HttpResponse("Hello, world!")
"""

def Home(request):
	return render(request, 'index.html')

def About(request):
	return render(request, 'about.html')