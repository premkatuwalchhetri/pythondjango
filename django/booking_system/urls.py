"""
URL configuration for booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views 
import room.urls
import contact.urls
import admin_panel.urls

urlpatterns = [
    path('', views.index, name='index'),  # Ensure the name 'index' is correctly defined
    path('django_admin/', admin.site.urls),
    path('booking/', include(room.urls)),
    path('contact/', include(contact.urls)),
    path('admin_panel/', include(admin_panel.urls)),
    path('add-room/', views.add_room, name='add_room'), 
    # Add the following lines for delete functionality
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),  # Single room delete
    path('delete-selected-rooms/', views.delete_selected_rooms, name='delete_selected_rooms'),  # Bulk delete
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
