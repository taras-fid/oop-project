from django.shortcuts import render
from .models import Ticket
# Create your views here.


def first_ticket_from_tickets(request):
    first_ticket = Ticket.objects.first()
    context = {'first_ticket': first_ticket}
    return render(request)
