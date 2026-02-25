from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha conecta a pasta 'loja' ao projeto principal
    path('', include('loja.urls')),
]
