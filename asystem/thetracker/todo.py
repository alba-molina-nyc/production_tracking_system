from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

# TODO: go to : asystem/thetracker/models.py and change setter_name to on_delete=models.SET(and send to a function that saves this item we are deleting to the admin user)
class Job:
    order_num = models.Charfield(max_length=275)
    SKU = models.CharField(max_length=275)
    num_items = models.IntegerField()
    num_stones = models.IntegerField()
    description_text = models.TextField()
    # setter_name = models.ForeignKey(User, on_delete=)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # this is what makes it show up on the admin page
    def __str__(self):
        return self.order_num + ' | ' + str(self.setter_name) + ' | ' + str(self.created)



# TODO: change DB to psql in asystem/asystem/settings.py
# TODO: add AWS DB 
# TODO: if have time make sure to style (maybe bootstrap?)
