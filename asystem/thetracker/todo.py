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
# TODO: 1st thing to do when back on this is figure out why this is not rendering on the web

#   <!-- <div class="row">
#     <ul>
#       {% for qs in queryset %}
#       {% if job.order_num is job.order_num %}

     
 
#         <li>
#           Order num: {{ job.order_num }}
#         </li>
#         {% elif job.sku is job.sku %}

#           <span>SKU: {{ job.SKU }}</span>
#           {% elif job.setter_name is job.setter_name %}
#           <span>Setter Name: {{ job.setter_name }}</span>
#           {% else job.created is job.created %}
#           <span>Date Created: {{ job.created }}</span>

#           {% endif %}

#         <hr />
#         {% endfor %}
    
#     </ul>
#   </div> -->

# def is_valid_queryparam(param):
#     return param != '' and param is not None

# def filter(request):
#     qs = Job.objects.all()
#     order_num = request.GET.get('order_num')
#     SKU = request.GET.get('SKU')
#     setter_name = request.GET.get('setter_name')
#     created = request.GET.get('created')

#     if is_valid_queryparam(order_num):
#         qs = qs.filter(order_num = order_num)
    
#     if is_valid_queryparam(SKU):
#         qs = qs.filter(SKU = SKU )
    
#     if is_valid_queryparam(setter_name):
#         qs = qs.filter(setter_name = setter_name)

#     if is_valid_queryparam(created):
#         qs = qs.filter(created = created)


#     return qs




# def filterView(request):
#     qs = filter(request)
#     context = {
#         'queryset': qs,
#         'jobs': Job.objects.all()}
#     return render(request, 'home.html', context)


#  <h1>Filter Jobs</h1>
#   <form method="GET" action=".">
#     <div class="form-row">
#       <div class="form-group col-12">
#           <div class="input-group">
#               <input class="form-control py-2 border-right-0 border" type="search" name="order_num" placeholder="Search by order..." />
#               <span class="input-group-append">
#                   <div class="input-group-text bg-transparent">
#                       <i class="fa fa-search"></i>
#                   </div>
#               </span>
#           </div>
#       </div>        
#   </div>
#   <div class="form-row">
#     <div class="form-group col-12">
#         <div class="input-group">
#             <input class="form-control py-2 border-right-0 border" type="search" name="SKU" placeholder="Search by SKU" />
#             <span class="input-group-append">
#                 <div class="input-group-text bg-transparent">
#                     <i class="fa fa-search"></i>
#                 </div>
#             </span>
#         </div>
#     </div>        
# </div>
# <div class="form-row">
#   <div class="form-group col-12">
#       <div class="input-group">
#           <input class="form-control py-2 border-right-0 border" type="search" name="setter_name" placeholder="Search by setter name" />
#           <span class="input-group-append">
#               <div class="input-group-text bg-transparent">
#                   <i class="fa fa-search"></i>
#               </div>
#           </span>
#       </div>
#   </div>        
# </div>
# <div class="form-row">
#   <div class="form-group col-12">
#       <div class="input-group">
#           <input class="form-control py-2 border-right-0 border" type="search" name="created" placeholder="Search Date Created" />
#           <span class="input-group-append">
#               <div class="input-group-text bg-transparent">
#                   <i class="fa fa-search"></i>
#               </div>
#           </span>
#       </div>
#   </div>        
# </div>
#   <button type="submit" class="btn btn-primary">Search</button>
#   </form>
#   <hr/>

#   {% endblock%}

  # path('', views.home, name='home'),
    # path('', filterView, name=' filterView'),

