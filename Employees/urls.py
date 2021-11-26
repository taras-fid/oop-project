from django.contrib import admin
from django.urls import path, include
from Employees import views


admin.autodiscover()

urlpatterns = [
    path('', include('Проект.urls')),
    path('employees', views.employees, name='employees'),
    path('hiring', views.hiring, name='hiring'),
    path('roles', views.roles, name='roles')
]