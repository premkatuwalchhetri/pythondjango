from django.shortcuts import render

from room.models import Room
# Create your views here.

def booking_section(request):
  rooms = Room.objects.all()
  data = {
    'rooms': rooms
  }
  return render(request, 'booking_section.html',data)

def book(request):
  return render(request, "book.html")