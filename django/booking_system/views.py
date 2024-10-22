from django.shortcuts import render, redirect, get_object_or_404
from room.models import Room
from category.models import Category
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')


def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        room_type = request.POST.get('room_type')
        price = request.POST.get('price')
        available_date = request.POST.get('available_date')

        image = request.FILES.get('image')  

        if image:
            room = Room(
                name=name,
                description=description,
                price=price,
                discount=0,  
                image=image,  
            )
            room.save()

            return redirect('dashboard_rooms')  # Redirect to rooms dashboard

    return render(request, 'admin_panel/add_room.html')


def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('dashboard_rooms')  


def delete_selected_rooms(request):
    if request.method == 'POST':
        selected_rooms = request.POST.getlist('room_select')  
        Room.objects.filter(id__in=selected_rooms).delete()  
        return redirect('dashboard_rooms') 
    
def delete_category(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    category.delete()
    return redirect('add_category')  


def delete_selected_categories(request):
    if request.method == 'POST':
        selected_categories = request.POST.getlist('category_select')  
        Category.objects.filter(id__in=selected_categories).delete()  
        return redirect('add_category') 