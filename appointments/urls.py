from django.urls import path
from . import views

app_name = 'appointments' 
urlpatterns = [
    path('new/', views.appointment_create, name='appointment_create'),
    path('list/', views.appointment_list, name='appointment_list'),
]
