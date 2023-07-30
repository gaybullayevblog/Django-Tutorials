from django.db import models

# Create your models here.

class Contact(models.Model):
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    parol = models.CharField(max_length=255)