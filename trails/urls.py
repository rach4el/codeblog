from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Add_a_Trail, name='trails'),  # Make sure this is correct
]