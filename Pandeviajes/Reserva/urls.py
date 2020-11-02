from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('Destinos/', views.Destinos, name='Destinos'),
    path('Pasajes/', views.Pasajes, name='Pasajes'),

   path('reserva/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detail'),

    path('reserva/', views.ReservaListView.as_view(), name='reserva')
    
]
urlpatterns+=[
    path('reserva/create/', views.ReservaCreate.as_view(), name= 'reserva_create'),
    path('reserva/<int:pk>/update/' ,views.ReservaUpdate.as_view(), name='reserva_update'),
    path('reserva/<int:pk>/delete/',views.ReservaDelete.as_view(), name='reserva_delete'),

]