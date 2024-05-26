from django.urls import path
from . import views

urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
    path('edit_submission/<int:submission_id>/', views.edit_submission, name='edit_submission'),
    path('confirm_delete/<int:submission_id>/', views.confirm_delete, name='confirm_delete'),
]