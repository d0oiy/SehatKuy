from django.urls import path
from . import views

urlpatterns = [
     path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('activity-log/', views.activity_log, name='activity_log'),
]
