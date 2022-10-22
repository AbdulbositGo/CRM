from django.urls import path
from .views import *


urlpatterns = [
    path("list/", lead_list, name='lead_list'),
    path("<pk>/detail/", lead_detail, name='lead_list'),
    path("create/", lead_create, name='lead_list'),
]
