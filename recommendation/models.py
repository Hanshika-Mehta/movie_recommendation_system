
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

class movies(models.Model):
    # Field name made lowercase.
    title = models.CharField(db_column='movie_Name', max_length=100)
    # Field name made lowercase.
    genre = models.CharField(db_column='genre', max_length=100)

class userData(models.Model):
    name = models.CharField(db_column='Name', max_length=30)
    email = models.EmailField(db_column='Email')
    mobile = models.IntegerField(db_column='Mobile')
    domain = models.CharField(db_column = 'Domain', max_length=100)
# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(db_column='Mobile',null=True,blank=TRUE,max_length=10)
    domain = models.CharField(db_column = 'Domain', max_length=100,null=True,blank=True)

    
