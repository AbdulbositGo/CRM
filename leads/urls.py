from django.urls import path
from .views import *


urlpatterns = [
    path("list/", lead_list, name='lead-list'),
    path("create/", lead_create, name='lead-create'),
    path("<pk>/detail/", lead_detail, name='lead-detail'),
    path("<pk>/update/", lead_update, name='lead-update'),
    path("<pk>/delete/", lead_delete, name='lead-delete'),
]
