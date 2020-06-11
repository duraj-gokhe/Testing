from django.db import models

# Create your models here.

class Person(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=500)
    Jwt = models.CharField(max_length=100)
    CreateDateTime = models.DateTimeField(auto_now_add=True)
    LastUpdateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName