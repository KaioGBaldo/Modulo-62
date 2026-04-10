from django.urls import path
from .views import home_async, home_sync

urlpatterns = [
    # Agora a página inicial (vazia) chama a home_async
    path('', home_async, name='async_root'), 
    path('sync/', home_sync, name='sync'),
    path('async/', home_async, name='async'),
]