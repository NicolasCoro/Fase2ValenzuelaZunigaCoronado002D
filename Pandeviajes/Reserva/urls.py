from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('Destinos/', views.Destinos, name='Destinos'),
    path('Pasajes/', views.Pasajes, name='Pasajes'),

    
]