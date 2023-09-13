from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    car = Car.objects.all()
    context = {'car': car}
    return render(request, 'index.html', context)