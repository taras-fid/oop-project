from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticketStore_main, name='ticketStore_main'),
    path('hot', views.ticketStore_hot, name='ticketStore_hot'),
]
