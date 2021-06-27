from django.shortcuts import render

from .models import City, Person

from django.db.models import Count


def show_persons(request):
    persons = Person.objects.select_related('city')
    return render(request, "city_person/home.html", {'persons': persons})


def show_cities(request):
    cities = City.objects.all().prefetch_related('persons')
    return render(request, "city_person/cities_list.html", {'cities': cities})

def show_biggest(request):
    biggest_cities = City.objects.prefetch_related('persons').annotate(num_persons=Count('persons')).order_by('-num_persons')
    return render(request, "city_person/biggest_cities.html", {'biggest_cities': biggest_cities[:5]})