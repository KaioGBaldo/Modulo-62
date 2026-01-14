from django.urls import path
from .views import execucao_sincrona, execucao_concorrente

urlpatterns = [
    path('sincrona/', execucao_sincrona),
    path('concorrente/', execucao_concorrente),
]
