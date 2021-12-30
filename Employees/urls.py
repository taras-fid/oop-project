from django.contrib import admin
from django.urls import path, include
from Employees import views


admin.autodiscover()

urlpatterns = [
    path('', views.index, name = 'employees_main'),
    path('employees', views.employees, name='employees'),
    path('hiring', views.hiring, name='hiring'),
    path('roles', views.roles, name='roles')
]