from django.urls import path
from . import views
urlpatterns = [ 
    path('contact/', views.contact, name="contact"),
    path('contact-store-contact/', views.store_contact, name="store_contact"),
    
]
