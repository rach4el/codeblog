from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dilhkd69z", 
    api_key = "377163352922742", 
    api_secret = "<your_api_secret>", # Click 'View Credentials' below to copy your API secret
    secure=True
)

