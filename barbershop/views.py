from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from .models import *
# from django.http import HttpResponse
# from django.template import loader

def home(req):
    # template = loader.get_template('home.html')
    # context = {'data':'result'}
    return render(req, "pages/home.html")

def story(req):
    return render(req, "pages/story.html")

def services(req):
    return render(req, "pages/services.html")

def price(req):
    return render(req, "pages/price.html")

# def contact(req):
#     contact = Contact.objects.all()
#     branche = Branche.objects.all()
#     context = {
#         "contact":contact,
#         "branche":branche }
#     return render(req, "pages/contact.html", context)

class Contact(ListView):
    model = Contact
    template_name = 'pages/contact.html'