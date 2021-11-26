from django.core.validators import RegexValidator, MinValueValidator, DecimalValidator
from django.db import models
from phone_field import PhoneField

import performance.models


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    patronymic = models.CharField('Patronymic', max_length=30)
    phone = PhoneField('Phone number')
    work_book = models.CharField('Number of the work book', max_length=9,
                                               validators=[RegexValidator(regex='[А-Я]{2}\\d{7}$')])
    email = models.EmailField('Email')
    address = models.CharField('Home address', max_length=50)
    date_of_birth = models.DateField('Date of birth')

    def __unicode__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Position(models.Model):
    position = models.CharField('Work position', max_length=50)


class Hiring(models.Model):
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    hiring_date = models.DateField('Hiring date')


class Role(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    poster_id = models.ForeignKey(performance.models.Poster, on_delete=models.CASCADE)
    name = models.CharField('Role name', max_length=30)
    fee = models.DecimalField(
        'Fee per role', decimal_places=2, max_digits=20,
        validators=[
            MinValueValidator(0.01)
        ]
    )
