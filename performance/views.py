from django.shortcuts import render
from django.http import HttpResponse
from .models import Performance

# Create your views here.

def main(request):
    return render(request, "performance/main.html")


def performance(request):
    performances = Performance.objects.all()
    return render(request, 'performance/performance.html', {'performances': performances})


def performance_to_be(request):
    return render(request, 'performance/performance_to_be.html')


def about(request):
    return render(request, 'performance/about.html')


def contact(request):
    return render(request, 'performance/contact.html')


