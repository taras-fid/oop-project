from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin_home')
]