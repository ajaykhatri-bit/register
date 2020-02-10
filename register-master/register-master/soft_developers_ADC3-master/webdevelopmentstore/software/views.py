from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App

# Create your views here.
#def App(request):
	#return HttpResponse("we are in development phase")

def homepage(request):
	return render(request=request, template_name="main/home.html", context={"apps": App.objects.all})

