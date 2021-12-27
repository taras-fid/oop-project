from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Ticket
from performance.models import *
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from datetime import date
from .forms import OrderForm
from .filters import PerformanceFilter, PosterFilter

# Create your views here.


def ticketStore_main(request):
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
    return render(request, 'ticketStore/ticketStore_hot.html', {'performances': performances, 'poster': poster, 'date': d})


def ticketStore_performance(request, pk):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticketStore_main')
        else:
            error = 'Замовлення заповненно некоректно'

    form = OrderForm()
    # performances = Performance.objects
    tickets = Ticket.objects.order_by('place')
    # for el in tickets:
    #     if not int(el.place) % 10:
    #         i = 0
    return render(request, 'ticketStore/ticketStore_performance.html', {'tickets': tickets, 'form': form,
                                                                        'error': error})


def ticketStore_form(request):
    return render(request, 'ticketStore/ticketStore_main.html')


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
