from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('create_temporary_user/', views.create_temporary_user, name='create_temporary_user'),
    path('appointments/', views.appointments, name='appointments'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
]
