from django.contrib import admin
from django.urls import path, include
from leads.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('lead/', include("leads.urls")),

]
