from django.shortcuts import render, redirect, get_object_or_404
from room.models import Room
from room.models import Category  # Import the Room model

def rooms(request):
    rooms = Room.objects.all()
    categories = Category.objects.all()  # Fetch all categories
    context = {
        'rooms': rooms,
        'categories': categories
    }
    return render(request, 'admin_panel/rooms.html', context)

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)  
    room.delete()  
    return redirect('rooms')


def index(request):
    return render(request, 'admin_panel/index.html')

def accounts(request):
    return render(request, 'admin_panel/accounts.html')

def add_room(request):
    return render(request, 'admin_panel/add_room.html')

def edit_room(request):
    return render(request, 'admin_panel/edit_room.html')

def login(request):
    return render(request, 'admin_panel/login.html')


