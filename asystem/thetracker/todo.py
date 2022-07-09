from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# TODO: go to : asystem/thetracker/models.py and change setter_name to on_delete=models.SET(and send to a function that saves this item we are deleting to the admin user)
class Job(models.Model):
    order_num = models.CharField(max_length=275)
    SKU = models.CharField(max_length=275)
    num_items = models.IntegerField()
    num_stones = models.IntegerField()
    description_text = models.TextField()
    setter_name = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_num + ' | ' + str(self.setter_name) + ' | ' + str(self.created)
    
    #TODO: gauge which return he wants
    def get_absolute_url(self):
        return reverse('add-job')
        # or -> to return to home and avoid passing in self.id 
        # return reverse('home') # to send back to home
        # or -> to return into the new job the user just created
        # return reverse('job-detail', args=(str(self.id)))

       



# TODO: change DB to psql in asystem/asystem/settings.py
# TODO: add AWS DB 
# TODO: if have time make sure to style (maybe bootstrap?)
