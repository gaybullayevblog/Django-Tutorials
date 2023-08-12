from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.
def main(req):
    item_list = Todo.objects.order_by("-date")
    if req.method == "POST":
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(req, "main.html", context=page)

def remove(req, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(req, "item removed !!!")
    return redirect('main')