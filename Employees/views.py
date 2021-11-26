from django.shortcuts import render
from .models import Employee, Hiring, Role


def index(request):
    return render(request, 'Employees/index.html')


def employees(request):
    output = Employee.objects.all()
    return render(request, 'Employees/employees.html', output)


def hiring(request):
    output = Hiring.objects.all()
    return render(request, 'Employees/hiring.html', output)


def roles(request):
    output = Role.objects.all()
    return render(request, 'Employees/roles.html', output)
