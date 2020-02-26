from django.db import models

# Create your models here.

class Person(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Jwt = models.CharField(max_length=100)
    CreateDateTime = models.DateTimeField()
    LastUpdateDateTime = models.DateTimeField()
