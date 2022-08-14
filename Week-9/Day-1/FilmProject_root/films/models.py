from platform import release
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('country', args=[self.id])



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.id])

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('director', args=[self.id])  


class Film (models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(default=date.today())
    created_in = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True)
    available_in = models.ManyToManyField(Country, related_name='films', blank=True)
    category = models.ManyToManyField(Category, related_name = 'films', blank = True)
    director = models.ManyToManyField(Director, related_name='films', blank = True)

    def __str__(self) -> str:
        return f"Title: {self.title}, Release date: {self.release_date}"

    def get_absolute_url(self):
        return reverse('film', args=[self.id])

