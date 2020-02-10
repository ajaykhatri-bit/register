from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import App
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
#from .forms import OurForm
from django.contrib import messages
from software.models import User
# Create your views here.



def user_register(request):
	if request.method == 'POST':
		userfname = request.POST.get('user_fname')
		userlname = request.POST.get('user_lname')
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('user_email')

	return render(request, "main/register.html", context={})



def user_logout(request):
	logout(request)
	return redirect('main:homepage')


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main:homepage')
		else:
			return HttpResponse("Wrong Credientials")
	else: 
		return render(request, "main/login.html", context={})
