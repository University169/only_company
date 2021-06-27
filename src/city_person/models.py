from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField("City name", max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField("Person name", max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='persons')

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name