from django.urls import path
from . import views

urlpatterns = [
    path('', views.Add_a_Trail, name='suggest'),
]
