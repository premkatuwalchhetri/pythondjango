from django.shortcuts import render, redirect, get_object_or_404
from room.models import Room
from category.models import Category   # Import the Room model

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

from category.models import Category
from category.forms import CategoryForm  # Assuming you've created this form

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:add_category') 
    else:
        form = CategoryForm()

    return render(request, 'admin_panel/add_category.html', {'form': form})

def delete_category(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)  
    category.delete()  
    return redirect('add_category')



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




