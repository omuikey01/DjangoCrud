from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    contact = models.IntegerField()
    password = models.CharField(max_length=100)
    confirm_pass = models.CharField(max_length=100)

class QueryModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null = True)
    query = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)