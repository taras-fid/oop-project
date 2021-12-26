from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticketStore_main, name='ticketStore_main'),
    path('hot', views.ticketStore_hot, name='ticketStore_hot'),
    path('<int:pk>', views.ticketStore_performance, name='ticketStore_performance'),
    path('form', views.ticketStore_performance, name='ticketStore_form'),
    path('filter/<int:pk>', views.performance_filter, name='performance_filter'),
]
