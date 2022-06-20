from django.urls import path
from . import views

urlpatterns = [
    path('create_team', views.create_team, name='create_team'),
    path('dividend', views.dividend, name='dividend'),
    path('bonus', views.bonus, name='bonus'),
]
