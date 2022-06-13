from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='desk_homepage'),
    
]
