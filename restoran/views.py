# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from .models import Contact


def home(req):
    # return HttpResponse("<h1>Home</h1>")
    # return JsonResponse({'text': 'Just rendering some JSON :)'})
    # context = {'name': 'Sardor'}
    return render(req, "pages/home.html")
    # return HttpResponse("Salom")

def about(req):
    return render(req, "pages/about.html")

def service(req):
    return render(req, "pages/service.html")

def menu(req):
    return render(req, "pages/menu.html")

def pages(req):
    return render(req, "pages/pages.html")

def booking(req):
    return render(req, "pages/booking.html")

def our_team(req):
    return render(req, "pages/our_team.html")

def testimonial(req):
    return render(req, "pages/testimonial.html")

def contact(req):
    # data = Contact.objects.all()
    # context = {'data': data}
    return render(req, "pages/contact.html")