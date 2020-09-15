from django.urls import path, re_path
from jobs.api.views import JobListCreateView, JobDetailUpdateDeleteView

app_name = 'jobs'

urlpatterns = [
    path('jobs', JobListCreateView.as_view(), name='job_list_create'),
    path('jobs/<int:pk>', JobDetailUpdateDeleteView.as_view(), name='job_detail_update_delete'),
]