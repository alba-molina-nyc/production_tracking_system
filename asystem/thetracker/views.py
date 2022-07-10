from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Job



# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = Job.objects.all()
    order_num = request.GET.get('order_num')
    SKU = request.GET.get('SKU')
    setter_name = request.GET.get('setter_name')
    created = request.GET.get('created')

    if is_valid_queryparam(order_num):
        qs = qs.filter(order_num = order_num)
    
    if is_valid_queryparam(SKU):
        qs = qs.filter(SKU = SKU )
    
    if is_valid_queryparam(setter_name):
        qs = qs.filter(setter_name = setter_name)

    if is_valid_queryparam(created):
        qs = qs.filter(created = created)


    return qs




def filterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'jobs': Job.objects.all()}
    return render(request, 'home.html', context)

class HomeView(ListView):
    model = Job
    template_name = 'home.html'





class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'

class AddJobView(CreateView):
    model = Job
    template_name = 'add_job.html'
    fields = '__all__'