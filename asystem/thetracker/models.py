from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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




