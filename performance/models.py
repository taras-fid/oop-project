from django.db import models

import django.core.validators as validators


# Create your models here.


class Rating(models.Model):
    description = models.TextField()
    min_age = models.IntegerField()


class Performance(models.Model):
    name = models.CharField(max_length=64)
    rating_id = models.ForeignKey(Rating, on_delete=models.SET_NULL)
    description = models.TextField
    author = models.CharField(max_length=64)
    duration = models.DurationField()
    genre_id = models.ForeignKey(Genre, on_delete=models.SET_NULL)
    price = models.DecimalField(validators=[
        validators.MinValueValidator(0.01),
        validators.DecimalValidator(decimal_places=2)
    ])

class Genre(models.Model):
    genre = models.TextField(max_length=32)

class Hall(models.Model):
    number = models.CharField(max_length=32)
    description = models.TextField


class Tier(models.Model):
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    level = models.IntegerField()
    number_of_seats = models.PositiveIntegerField()


class Poster(models.Model):
    performance_id = models.ForeignKey(Performance, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    hall_id = models.ForeignKey(Hall, on_delete=models.SET_NULL)
