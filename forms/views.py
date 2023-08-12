from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.
def main(req):
    return render(req, "main.html", context={"data": 200})

def forms(req):
    if req.method == "POST":
        form = MyForm(req.POST)

        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = MyForm()

    return render(req, "forms.html", context={"form": form})