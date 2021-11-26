from django.contrib import admin
from django.urls import path, include
#from requisite import views
#from . import views
from Employees import views
from django.conf.urls import url


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Проект.urls')),
    path('employees', views.employees, name='employees'),
    path('hiring', views.hiring, name='hiring'),
    path('roles', views.roles, name='roles'),

    #url('$', views.index, name='index')
]