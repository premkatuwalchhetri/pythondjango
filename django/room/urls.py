

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.booking_section, name='booking_section'),
    path('book/', views.book, name='book'),
    path('book-stay/', views.book_stay, name='book_stay'),  # Use a different URL for the actual booking submission
]

