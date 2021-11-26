"""Проект URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from requisite import views
#from . import views
from Employees import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('Проект.urls')),
    path('', views.index),
    path('requisite/', views.index),
    path('employees/', views.employees)

    #url('$', views.index, name='index')
    #url('$', views.index, name='index')
    #path('catalog/', include('catalog.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
