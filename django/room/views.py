from django.shortcuts import render, redirect
from .forms import BookingForm
from django.http import HttpResponse

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

def book_stay(request):
    if request.method == 'POST':
        print(request.POST)  
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Congrats! Your room has been reserved.')
        else:
            return HttpResponse(f'Error: {form.errors}', status=400)
    else:
        return HttpResponse('Invalid request method.', status=405)




