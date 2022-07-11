import django_filters
from .models import *

# build python class that is going to build filter for us
class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = '__all__'