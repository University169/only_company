from django.shortcuts import render

from .models import City, Person, Event

from django.db.models import Count, F

from django.core.paginator import Paginator


def show_persons(request):
    persons = Person.objects.select_related('city')
    return render(request, "city_person/home.html", {'persons': persons})


def show_cities(request):
    cities = City.objects.all().prefetch_related('persons')
    return render(request, "city_person/cities_list.html", {'cities': cities})

def show_biggest(request):
    biggest_cities = City.objects.prefetch_related('persons').annotate(num_persons=Count('persons')).order_by('-num_persons')
    return render(request, "city_person/biggest_cities.html", {'biggest_cities': biggest_cities[:5]})

def event_list(request):
    events_list = Event.objects.annotate(duration_time=F('end_date')-F('start_date')).order_by('duration_time')
    paginator = Paginator(events_list, 3)  # 3 события на каждой странице
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)
    return render(request, 'city_person/event_list.html', {'events': events})