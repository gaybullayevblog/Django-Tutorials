from django.shortcuts import render

# Create your views here.

def student(req):
    return render(req, "main.html", context={"data": 200})