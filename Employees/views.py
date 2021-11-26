from django.shortcuts import render
#from . import models
from .models import Employee
from django.http import HttpResponse


def index(request):
    latest_question_list = Employee.objects.all()
    #context = {'latest_question_list': latest_question_list}
    output = ', '.join([q.first_name for q in latest_question_list])
    #return HttpResponse(output)

    return render(request, 'Employees/index.html')


def employees(request):
    return render(request, 'Employees/employees.html')
    #return HttpResponse(render(request, 'Employees/index.html', context))
# def index(request):
#   latest_question_list = Employee.objects.order_by('first_name')[:5]
#  output = ', '.join([q.last_name for q in latest_question_list])
# return HttpResponse(output)
# Create your views here.
