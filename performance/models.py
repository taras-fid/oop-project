from django.db import models


# Create your models here.
class Rating(models.Model):
    description = models.CharField(max_length=265)
    min_age = models.IntegerField()


class Performance(models.Model):
    name = models.CharField(max_length=64)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL)
    description = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
    producer = models.ForeignKey()
    duration = models.DurationField()
    genre = models.TextField(max_length=32)
    price = models.DecimalField()


class Hall(models.Model):
    number = models.CharField(max_length=32)
    description = models.CharField(max_length=256)


class Tier(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    level = models.IntegerField()
    number_of_seats = models.IntegerField()


class Poster(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.SET_NULL())
    date = models.DateTimeField()
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL)
