from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Job
from .filters import JobFilter




class HomeView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context



# https://django-filter.readthedocs.io/en/stable/guide/usage.html
# https://www.youtube.com/watch?v=G-Rct7Na0UQ&ab_channel=DennisIvy
# https://www.youtube.com/results?search_query=get+input+value+on+server+side+and+filter+database+django

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    fields = '__all__'

class AddJobView(CreateView):
    model = Job
    template_name = 'add_job.html'
    fields = '__all__'