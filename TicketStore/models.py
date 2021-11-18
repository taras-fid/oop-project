from django.db import models
from django.core.validators import MinValueValidator, DecimalValidator

import performance.models


class Ticket(models.Model):
    price = models.DecimalField(
        validators=[
            MinValueValidator(0.01),
            DecimalValidator(decimal_places=2)
        ]
     )
    place = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
     )
    availability = models.BooleanField()
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    tier_id = models.ForeignKey(performance.models.Tier, on_delete=models.CASCADE)
