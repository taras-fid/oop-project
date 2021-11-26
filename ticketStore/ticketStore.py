from decimal import Decimal
from django.conf import settings
from .models import Ticket


class TicketStore(object):
    def __init__(self, request):
        self.session = request.session
        ticketStore = self.session.get(settings.TICKETSTORE_SESSION_ID)
        if not ticketStore:
            ticketStore = self.session[settings.TICKETSTORE_SESSION_ID] = {}
        self.ticketStore = ticketStore

    def __iter__(self):
        ticket_ids = self.ticketStore.keys()
        tickets = Ticket.objects.filter(place__in=ticket_ids)

        ticketStore = self.ticketStore.copy()
        for ticket in tickets:
            ticketStore[str(ticket.place)]['ticket'] = ticket

        for item in ticketStore.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, ticket, quantity=1, update_quantity=False):
        place = str(Ticket.place)
        if place not in self.ticketStore:
            self.ticketStore[place] = {'quantity': 0, 'price': str()}
        if update_quantity:
            self.ticketStore[ticket_id]['quantity'] = quantity
        else:
            self.ticketStore[ticket_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.ticketStore:
            del self.ticketStore[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.ticketStore.values())

    def clear(self):
        del self.session[settings.TICKETSTORE_SESSION_ID]
        self.save()
