from django.contrib import admin

from .models import City, Person, Event
# Register your models here.

admin.site.register(City)
admin.site.register(Person)
admin.site.register(Event)
