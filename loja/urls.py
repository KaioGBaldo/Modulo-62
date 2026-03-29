from django.urls import path
from .views import home_async, home_sync

urlpatterns = [
    path('sync/', home_sync, name='sync'),
    path('async/', home_async, name='async'),
]
