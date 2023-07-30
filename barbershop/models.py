from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=402)
    email = models.CharField(max_length=402)
    time = models.CharField(max_length=402)
    link = models.CharField(max_length=402)

class Branche(models.Model):
    name = models.CharField(max_length=402)
    location = models.CharField(max_length=402)
