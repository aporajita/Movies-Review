from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Viewer, Movies, Category
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def signupPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'movies/signup.html', context)

@unauthenticated_user
def loginPage(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('movies')
			else:
				messages.info(request, 'Username OR password is incorrect')


		return render(request, 'movies/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


def movies(request):

    movies = Movies.objects.all()
    category = Category.objects.all()
    context = {
        'movies': movies, 
        'category': category
        }
    return render(request, 'movies/movies.html', context)

def categoryList(request, id):
        
    movies = Movies.objects.all().filter(category_id = id)
    category = Category.objects.all()
    context = {
        'movies': movies,
        'category': category
        }
    return render(request, 'movies/category.html', context)

def Snippet(request,id):

    movies = Movies.objects.all().filter(id=id)
    category = Category.objects.all()
    context = {
        'movies': movies,
        'category': category
        }
    return render(request, 'movies/snippet.html', context)

