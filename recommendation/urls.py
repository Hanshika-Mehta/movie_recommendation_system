from django.contrib import admin
from django.urls import path , include
from recommendation import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('profile', views.profile,name='profile'),
    path('to_do', views.to_do,name='to_do'),
    path('allmovies', views.allmovies,name='allmovies'),
    path('login', views.loginUser,name='login'),
    path('logout', views.logoutUser,name='logout'),
]
