from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('admin_panel:rooms')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CategoryForm()

    return render(request, 'admin_panel/add-category.html', {'form': form})

