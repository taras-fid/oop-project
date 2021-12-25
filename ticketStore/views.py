from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ticket
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View


# Create your views here.


def ticketStore_main(request):
    tickets = Ticket.objects.order_by('availability', 'place')
    # for el in tickets:
    #     if not int(el.place) % 10:
    #         i = 0
    data = {'tickets': tickets}
    return render(request, 'ticketStore/ticketStore_main.html', context=data)


def ticketStore_add(request):
    pass


def ticketStore_delete(request):
    pass


def ticketStore_hot(request):
    return render(request, 'ticketStore/ticketStore_hot.html')


def ticketStore_1(request):
    tickets = Ticket.objects.order_by('availability', 'place')
    # for el in tickets:
    #     if not int(el.place) % 10:
    #         i = 0
    data = {'tickets': tickets}
    return render(request, 'ticketStore/ticketStore_1.html', context=data)
