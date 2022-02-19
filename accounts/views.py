from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def register(request):
	if request.method == 'POST': #Register User
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		if password == password2: # Проверка на совпадение паролей
			if User.objects.filter(username=username).exists(): #проверка есть ли уже такой пользователь
				messages.error(request, ' That username alredy exists')
			return redirect('register')
		else:
			if User.objects.filter(email=email).exists(): #проверка используется ли уже такой емейл
				messages.error(request, ' That email alredy exists')
				return redirect('register')
			else:
				pass
				
	else:
		return render(request, 'accounts/register.html')

def login(request):
	if request.method == 'POST': #Login user
		return
	else:
		return render(request, 'accounts/login.html')
def logout(request):
	return redirect('index')
def dashboard(request):
	return render(request, 'accounts/dashboard.html')