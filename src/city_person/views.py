from django.shortcuts import render

from .models import City, Person


def show_persons(request):
    persons = Person.objects.select_related('city')
    return render(request, "city_person/home.html", {'persons': persons})


def show_cities(request):
    cities = City.objects.all().prefetch_related('persons')
    return render(request, "city_person/cities_list.html", {'cities': cities})

def show_biggest(request):
    biggest_cities = City.objects.all().prefetch_related('persons')
    # посчитать количество людей в каждом городе
    # data = [('Moscow', 31, [persons]), ('Kaliningrad',153, [persons]), ('SPb',82, [persons])]
    # Вывести 5 первых элементов: id - Город - Кол-во жителей - Сами жители
    return render(request, "city_person/biggest_cities.html", {'biggest_cities': biggest_cities})