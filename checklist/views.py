from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.order_by("id")

    con = {'tasks': tasks}

    return render(request, 'index.html', con)


def add(request):
    item = Task(name=request.POST["name"])
    item.save()
    return redirect("/")


def delete(request):
    item = Task.objects.get(id=request.POST["id"])
    if item:
        item.delete()
    return redirect("/")
