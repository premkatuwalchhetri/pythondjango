from django.shortcuts import render, redirect, get_object_or_404
from room.models import Room
from django.http import HttpResponse
from category.models import Category   # Import the Room model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
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


@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'admin_panel/index.html')


@login_required(login_url='/admin/login/')
def accounts(request):
    return render(request, 'admin_panel/accounts.html')

def add_room(request):
    return render(request, 'admin_panel/add_room.html')

def edit_room(request):
    return render(request, 'admin_panel/edit_room.html')

def admin_login(request):
    if request.method == "POST":
        #here will be login process
        print("\n\n","method_name is:", request.method,request.POST,"  ***************\n\n")
        username = request.POST['username']
        password = request.POST['password']
   
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            print(" user data get success ")
            return HttpResponse(f"you are going  to login with {username} and {password}")
        else:
            print("invalid password and username")
            return HttpResponse(f"invalid password and username")
        
    else:
        return render(request,"admin_panel/login.html")




