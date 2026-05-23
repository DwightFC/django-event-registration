"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='events/register/', permanent=False)),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
]
