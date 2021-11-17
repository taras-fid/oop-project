from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    price = models.PositiveIntegerField(
        default=10,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    place = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(150),
            MinValueValidator(1)
        ]
     )
    availability = models.BooleanField()
    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE)
    tier_id = models.ForeignKey(Tier, on_delete=models.CASCADE)
