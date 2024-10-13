from django.shortcuts import render, redirect, get_object_or_404
from room.models import Room  # Import your Room model
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

        # Handle the uploaded image
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)  # Save the image
        uploaded_file_url = fs.url(filename)  # Get the URL of the uploaded file

        # Create a new Room object
        room = Room(
            name=name,
            description=description,
            price=price,
            discount=0,  # Set a default value or get from the form
            image=uploaded_file_url,
        )
        room.save()

        return redirect('dashboard_rooms')  # Redirect to rooms page after saving

    return render(request, 'admin_panel/add_room.html')

# New delete view for a single room
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('dashboard_rooms')  # Redirect to the rooms page

# New delete view for selected rooms
def delete_selected_rooms(request):
    if request.method == 'POST':
        selected_rooms = request.POST.getlist('room_select')  # Get selected room IDs
        Room.objects.filter(id__in=selected_rooms).delete()  # Bulk delete the selected rooms
        return redirect('dashboard_rooms')  # Redirect to the rooms page
