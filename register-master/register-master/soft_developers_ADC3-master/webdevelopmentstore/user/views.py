from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import App
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
#from .forms import OurForm
from django.contrib import messages
from software.models import User
# Create your views here.



def user_register(request):
	if request.method == 'POST':
		userfname = request.POST['user_fname']
		userlname = request.POST['user_lname']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['user_email']
		print(request.POST)
		User.objects.create(user_fname=userfname,password=password, user_lname=userlname, username=username,  user_email=email)

	return render(request, "main/register.html", context={})



def user_logout(request):
	logout(request)
	return redirect('/')


def user_login(request):
	if request.method == 'get':
		username = request.get['username']
		password = request.get['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main:homepage')
		else:
			return HttpResponse("Wrong Credientials")
	else: 
		return render(request, "main/login.html", context={})
