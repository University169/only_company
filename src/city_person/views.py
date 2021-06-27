from django.views.generic.list import ListView

from .models import City, Person

class PersonsView(ListView):
    model = Person
    template_name = 'city_person/home.html'
    context_object_name = 'persons'