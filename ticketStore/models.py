from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, DecimalValidator
import performance.models


class Ticket(models.Model):
    price = models.DecimalField('Ticket price', decimal_places=2, max_digits=10,
                                validators=[
                                    MinValueValidator(0.01),
                                ]
                                )
    place = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    availability = models.BooleanField('Availability')
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    tier_id = models.ForeignKey(performance.models.Tier, on_delete=models.CASCADE)


class Order(models.Model):
    name = models.CharField('Name', max_length=64)
    phone = models.CharField('Phone', max_length=64)
    mail = models.CharField('Mail', max_length=64)
    tickets = ArrayField(ArrayField(models.IntegerField('Tickets')))