from django.urls import path
from galeria.views import index, imagem, buscar
from . import views

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<int:foto_id>', imagem, name = 'imagem'),
    path('buscar', buscar, name = 'buscar'),
    path('buscar/', views.buscar, name='buscar'),
]