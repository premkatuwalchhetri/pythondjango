from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),  # Home page
    path('accounts/', views.accounts, name='dashboard_accounts'),  # Corrected to point to accounts view
    path('add_room/', views.add_room, name='dashboard_add_room'),  # Corrected add_room view
    path('edit_room/', views.edit_room, name='edit_room'),  # Corrected to point to edit_room view
    path('login/', views.login, name='dashboard_login'),  # Corrected to point to login view
    path('rooms/', views.rooms, name='dashboard_rooms'),  # Rooms page
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),
]   

