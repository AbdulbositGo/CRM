from django.urls import path
from .views import AgentListView

urlpatterns = [
    path('list/', AgentListView.as_view(), name='agent-list')
]
