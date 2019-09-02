from django.db import models
import csv

# Create your models here.
class Search(models.Model):
    cities = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    city = models.TextField(max_length = 50)
    growth = models.CharField(max_length = 10)
    latitude = models.CharField(max_length = 20)
    longitude = models.CharField(max_length = 20)
    population = models.IntegerField(max_length = 10)
    rank = models.IntegerField(max_length = 1000)
    state = models.CharField(max_length = 10)
    timezone = models.CharField(max_length = 10)

    def __str__(self):
        return self.city
