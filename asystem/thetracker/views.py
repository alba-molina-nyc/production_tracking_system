from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Job

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Job
    template_name = 'home.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'