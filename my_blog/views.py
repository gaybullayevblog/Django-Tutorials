# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Contact


def home(req):
    # return HttpResponse("<h1>Home</h1>")
    # return JsonResponse({'text': 'Just rendering some JSON :)'})
    context = {'name': 'Sardor'}
    return render(req, "pages/home.html", context)
    # return HttpResponse("Salom")

def about(req):
    return render(req, "pages/about.html")

def portfolio(req):
    return render(req, "pages/portfolio.html")

def blog(req):
    return render(req, "pages/blog.html")

def contact(req):
    data = Contact.objects.all()
    context = {'data': data}
    return render(req, "pages/contact.html", context)