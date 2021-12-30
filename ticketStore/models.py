from django.db import models
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
    availability = models.BooleanField('Avail7ability')
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    tier_id = models.ForeignKey(performance.models.Tier, on_delete=models.CASCADE)
