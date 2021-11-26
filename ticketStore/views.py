from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ticket
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View


# Create your views here.


# TODO доделать хтмл и мозг для корзины(пока что сырой мозги пустая форма)
def ticketStore_main(request):
    return render(request, "ticketStore/ticketStore_main.html")


def ticketStore_add(request):
    pass


def ticketStore_delete(request):
    pass


def ticketStore_hot(request):
    return render(request, "ticketStore/ticketStore_hot.html")
