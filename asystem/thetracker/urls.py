from django.urls import path
# from . import views
from .views import HomeView, JobDetailView, AddJobView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('add_job', AddJobView.as_view(), name='add-job'),
]
