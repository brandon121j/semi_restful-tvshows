from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return redirect("/shows")


def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }

    return render(request, "index.html", context)


def newshows(request):
    return render(request, "newshow.html")


def addshows(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        all_shows = Show.objects.all()
        show_created = all_shows.create(title=request.POST['title'], network=request.POST['network'],
                                        release_date=request.POST['releasedate'], description=request.POST['description'])

    return redirect(f'/shows/{show_created.id}')


def editshows(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
    }
    return render(request, "editshow.html", context)


def edit(request, id):
    singleshow = Show.objects.get(id=id)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{singleshow.id}/edit')
    else:
        singleshow.title = (request.POST['title'])
        singleshow.network = (request.POST['network'])
        singleshow.release_date = (request.POST['releasedate'])
        singleshow.description = (request.POST['description'])
        singleshow.save()
        return redirect(f'/shows/{singleshow.id}')


def destroy(request, id):
    this_show = Show.objects.get(id=id)
    this_show.delete()
    return redirect("/shows")


def singleshow(request, id):
    context = {
        "one_show": Show.objects.get(id=id)
    }

    return render(request, "singleshow.html", context)
