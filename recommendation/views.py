from tabnanny import check
from typing_extensions import dataclass_transform
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from recommendation.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# from django.contrib.auth.models import User
# from django.contrib.auth import logout , authenticate , login
import pandas as pd 

# password from text user is 8118859092
#username for the test user is hanshika



def loginUser(request):
   
    if request.method=="POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(request,username=username, password=password)


        if user is not None:
            # A backend authenticated the credentials
            login(request , user ,backend=None)
            print("login successful")
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {})
    
    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect("/login")
    

def index(request):
    # return redirect("loginapp:about")
    #to create entries in the databaase
    # user1 = userData(name = "Harshit", email = "harp@ab.com", mobile = 8123456789, domain = "Action|Drama")
    # user1.save()
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')
    

def contact(request):
    #Read excel sheet (Dataset)
    # df = pd.read_csv('movies1.csv')
    # for title , genres in zip(df.title, df.genres):
    #         models = movies(title = title , genre = genres)
    #         models.save()
    return render(request, 'contact.html')

# movieId,title,genres

def to_do(request):
   
    id = userData.objects.filter(mobile = request.user.username)[0].id
    querydomain = list(userData.objects.get(pk=id).domain.replace('|', ',').split(","))
    for domain in querydomain:
        movielist = []
        movie1 = movies.objects.all()
        for movie in movie1:
            if (movie.genre == domain):
                movielist.append({'title': movie.title, 'genre': movie.genre})
        # print(movielist)
    return render(request, 'to_do.html', {'data':movielist})
    
def dashboard(request):
    id = userData.objects.filter(mobile = request.user.username)[0].id
    querydomain = list(userData.objects.get(pk=id).domain.replace('|', ',').split(","))
    print(id)
    for domain in querydomain:
        movielist = []
        movie1 = movies.objects.all()
        for movie in movie1:
            if (movie.genre == domain):
                movielist.append({'title': movie.title, 'genre': movie.genre})
        print(movielist)

    return render(request, 'dashboard.html', {'data': movielist})

def profile (request):
    id = request.GET.get('id')
    data = {'profiledata': userData.objects.get(pk=id)}
    return render(request, 'profile.html', {'data':data})


def allmovies(request):
    genre = request.GET.get('genre')
    movielist = []
    movie1 = movies.objects.all()
    for movie in movie1:
        if (movie.genre == genre):
            movielist.append({'title': movie.title, 'genre': movie.genre})
    print(movielist)
    return render(request, 'movies.html',{'data':movielist})


# Create your views here.
