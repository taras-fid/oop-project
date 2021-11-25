from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Performance, Rating, Genre, Hall, Tier, Poster
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
# Create your views here.


def main(request):
    return render(request, "performance/main.html")


def performance(request):
    performances = Performance.objects.order_by('-price')
    return render(request, 'performance/performance.html', {'performances': performances})


def performance_to_be(request):
    return render(request, 'performance/performance_to_be.html')


def about(request):
    return render(request, 'performance/about.html')


def contact(request):
    return render(request, 'performance/contact.html')


class PerformanceList(ListView):
    model = Performance


class Search(ListView): #TODO ne rabotayet(nado dodelat`)

    def get_queryset(self):
        return Performance.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
