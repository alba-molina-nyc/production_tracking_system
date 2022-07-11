import django_filters
from .models import Job

# this version uses a dictionary to match items that "contain"
class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'order_num' : ['icontains'],
            'SKU' : ['icontains'],
            'num_items' : ['icontains'],
            'num_stones' : ['icontains'],
            'description_text' : ['icontains'],
            'created' : ['icontains'],
            'updated' : ['icontains'],
        }



# build python class that is going to build filter - this version only shows exact search
# class JobFilter(django_filters.FilterSet):
#     class Meta:
#         model = Job
#         fields = '__all__'