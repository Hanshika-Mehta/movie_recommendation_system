from typing_extensions import dataclass_transform
from django.shortcuts import render, HttpResponse 
from recommendation.models import *
import pandas as pd 

def index(request):
    # return redirect("loginapp:about")
    # user1 = userData(name = "Somya", email = "som@ab.com", mobile = 81124228, domain = "Romance")
    # user1.save()
    return render(request, 'index.html')
def about(request):
    return render(request, 'about_us.html')
    

def contact(request):
    # df = pd.read_csv('movies1.csv')
    # for title , genres in zip(df.title, df.genres):
    #         models = movies(title = title , genre = genres)
    #         models.save()
    return render(request, 'contact.html')

# movieId,title,genres

def to_do(request):
    # print("get request = ",request.GET)
    id = 10
    # print("hello id = ",id)
    querydomain = list(userData.objects.get(pk=id).domain.replace('|', ',').split(","))
    for domain in querydomain:
        movielist = []
        movie1 = movies.objects.all()
        for movie in movie1:
            if (movie.genre == domain):
                movielist.append({'title': movie.title, 'genre': movie.genre})
        print(movielist)
    return render(request, 'to_do.html', {'data':movielist})
    
def dashboard(request):
    id = request.GET.get('id')
    querydomain = list(userData.objects.get(pk=id).domain.replace('|', ',').split(","))
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
