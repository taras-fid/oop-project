from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ticket
from performance.models import Performance, Poster
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from datetime import date


# Create your views here.


def ticketStore_main(request):
    performances = Performance.objects.order_by('-price')
    return render(request, 'ticketStore/ticketStore_main.html', {'performances': performances})


def ticketStore_add(request):
    pass


def ticketStore_delete(request):
    pass


def ticketStore_hot(request):
    today = date.today()
    d = today.strftime("%Y/%m/%d")
    performances = Performance.objects.order_by('-price')
    poster = Poster.objects.order_by('id')
    return render(request, 'ticketStore/ticketStore_hot.html', {'performances': performances, 'poster': poster, 'date': d})



def ticketStore_performance(request, pk):
    performances = Performance.objects
    tickets = Ticket.objects.order_by('availability', 'place')
    # for el in tickets:
    #     if not int(el.place) % 10:
    #         i = 0
    data = {'tickets': tickets, 'performances': performances}
    return render(request, 'ticketStore/ticketStore_performance.html', context=data)
