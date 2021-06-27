from django.shortcuts import render

from .models import City, Person


def show_persons(request):
    persons = Person.objects.select_related('city')
    return render(request, "city_person/home.html", {'persons': persons})