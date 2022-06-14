from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='desk'),
    path('dashboard', views.dashboard, name='dashboard'),
    
]
