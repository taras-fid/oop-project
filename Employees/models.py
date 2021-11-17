from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator


class Employee(models.Model):
    full_name = models.CharField('Full name', max_length=30)
    phone = PhoneField('Phone number')
    work_book = RegexValidator('Number of the work book', regex='[А-Я]{2}\\d{7}$')
    email = models.EmailField()
    address = models.CharField('Home address', max_length=50)
    position = models.CharField('Work position', max_length=50)
    date_of_birth = models.DateField('Date of birth')
    hiring_date = models.DateField('Hiring date')


class Role(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE)
    name = models.CharField('Role name', max_length=30)
    fee = models.PositiveIntegerField('Hourly fee per role')
