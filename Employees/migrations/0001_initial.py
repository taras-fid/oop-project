# Generated by Django 3.2.9 on 2021-12-25 17:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Patronymic')),
                ('phone', phone_field.models.PhoneField(max_length=31, verbose_name='Phone number')),
                ('work_book', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(regex='[А-Я]{2}\\d{7}$')], verbose_name='Number of the work book')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=50, verbose_name='Home address')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, verbose_name='Work position')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Role name')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Fee per role')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee')),
                ('poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.poster')),
            ],
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiring_date', models.DateField(verbose_name='Hiring date')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employees.employee')),
                ('position_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employees.position')),
            ],
        ),
    ]
