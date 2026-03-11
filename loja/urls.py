from django.urls import path
from . import views

urlpatterns = [
    # Rota para disparar o contador
    path('testar-contador/', views.contador_terminal, name='contador_terminal'),
]
