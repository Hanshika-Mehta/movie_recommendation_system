from django.shortcuts import render, HttpResponse 
from recommendation.models import *
import pandas as pd 

def index(request):
    # return redirect("loginapp:about")
    user1 = userData(name = "Deepesh", email = "12@ab.com", mobile = 12345, domain = "Action")
    user1.save()
    return render(request, 'index.html')
def about(request):
    return render(request, 'about_us.html')
    

def contact(request):
    return render(request, 'contact.html')
    
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

# Create your views here.
