from django.shortcuts import render

from .models import City, Person


def show_persons(request):
    persons = Person.objects.select_related('city')
    return render(request, "city_person/home.html", {'persons': persons})


def show_cities(request):
    cities = City.objects.all().prefetch_related('persons')
    return render(request, "city_person/cities_list.html", {'cities': cities})