from django.urls import path
from .views import (
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, lead_list, lead_create, lead_delete, lead_detail, lead_update
)


urlpatterns = [
    path("list/", LeadListView.as_view(), name='lead-list'),
    path("create/", LeadCreateView.as_view(), name='lead-create'),
    path("<pk>/detail/", LeadDetailView.as_view(), name='lead-detail'),
    path("<pk>/update/", LeadUpdateView.as_view(), name='lead-update'),
    path("<pk>/delete/", lead_delete, name='lead-delete'),
]
