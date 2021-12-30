from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Ticket, Ticket_ordered, Order
from performance.models import *
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from .forms import OrderForm
from .filters import PerformanceFilter, PosterFilter
import numpy as np
from datetime import date

# Create your views here.
global ticket_order
tickets_order = []


def ticketStore_main(request, pk=None):
    if pk == 'cancel':
        tickets_const = Ticket.objects.order_by('place')
        numpy_array = np.array(tickets_order)
        transpose = numpy_array.T
        tickets_order_output = transpose.tolist()
        for ticket in tickets_const:
            for el in tickets_order_output:
                for poster_el in tickets_order_output[0]:
                    for place_el in tickets_order_output[1]:
                        tickets_const.filter(place=place_el, poster_id_id=poster_el).update(availability=1)
        tickets_order.clear()

    poster = Poster.objects.order_by('id')
    myFilter = PosterFilter(request.GET, queryset=poster)
    poster = myFilter.qs
    return render(request, 'ticketStore/ticketStore_main.html', {'poster': poster, 'myFilter': myFilter})


def ticketStore_add(request):
    pass


def ticketStore_delete(request):
    pass


def ticketStore_hot(request):
    today = date.today()
    d = today.strftime("%Y/%m/%d")
    performances = Performance.objects.order_by('-price')
    poster = Poster.objects.order_by('id')
    return render(request, 'ticketStore/ticketStore_hot.html',
                  {'performances': performances, 'poster': poster, 'date': d})


def ticketStore_performance(request, pk=None):
    tickets_const = Ticket.objects.order_by('place')
    return render(request, 'ticketStore/ticketStore_performance.html', {'tickets': tickets_const, 'pk': pk,
                                                                        'tickets_order': tickets_order})


def ticketStore_order(request, pk, pkt=None):
    tickets_const = Ticket.objects.order_by('place')
    for el in tickets_const:
        if el.place == pkt and el.poster_id_id == pk:
            tickets_const.filter(place=pkt, poster_id_id=pk).update(availability=0)
            if not [pk, pkt] in tickets_order:
                tickets_order.append([pk, pkt])
    return render(request, 'ticketStore/ticketStore_order.html', {'tickets': tickets_const, 'pk': pk, 'pkt': pkt,
                                                                  'tickets_order': tickets_order})


def ticketStore_form(request):
    error = ''
    order_price = 0
    tickets_const = Ticket.objects.all()
    numpy_array = np.array(tickets_order)
    transpose = numpy_array.T
    tickets_order_output = transpose.tolist()
    today = date.today()
    date1 = today.strftime("%Y-%m-%d")
    for i in range(len(tickets_order_output[0])):
        order_price += tickets_const.get(poster_id_id=tickets_order_output[0][i], place=1).price
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            orders = Order.objects.order_by('-id')
            order = orders[0]
            Order.objects.filter(id=order.id).update(price=order_price)
            Order.objects.filter(id=order.id).update(date=date1)
            # [[1,1,1], [38,39,40]]
            for i in range(len(tickets_order_output[1])):
                Ticket_ordered.objects.create(
                    order=order,
                    place=tickets_order_output[1][i],
                    poster_id_id=tickets_const.get(place=tickets_order_output[1][i], poster_id_id=tickets_order_output[0][i]).poster_id_id,
                    price=tickets_const.get(place=tickets_order_output[1][i], poster_id_id=tickets_order_output[0][i]).price,
                    tier_id=tickets_const.get(place=tickets_order_output[1][i], poster_id_id=tickets_order_output[0][i]).tier_id_id)
            tickets_order.clear()
            return redirect('ticketStore_main')
        else:
            error = 'Замовлення заповненно некоректно'
    form = OrderForm()
    return render(request, 'ticketStore/ticketStore_form.html', {'form': form, 'error': error,
                                                                 'tickets_order': tickets_order})


def performance_filter(request, pk):
    poster = Poster.objects.all()
    if pk == 1:
        poster = poster.order_by('performance_id__price')
    if pk == 2:
        poster = poster.order_by('performance_id__duration')
    if pk == 3:
        poster = poster.order_by('date')
    myFilter = PosterFilter(request.GET, queryset=poster)
    poster = myFilter.qs
    return render(request, 'ticketStore/ticketStore_main.html', {'poster': poster, 'myFilter': myFilter})


def requisite(request):
    performances = Performance.objects.all()
    myFilter = PerformanceFilter(request.GET, queryset=performances)
    performances = myFilter.qs
    return render(request, 'ticketStore/ticketStore_main.html', {'performances': performances, 'myFilter': myFilter})
