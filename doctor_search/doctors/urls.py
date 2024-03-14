from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('create/', views.create_doctor, name='create_doctor'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit_doctor, name='edit_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
]
