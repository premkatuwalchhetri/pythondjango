from django.shortcuts import render

# Create your views here.

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

def rooms(request):
    return render(request, 'admin_panel/rooms.html')
