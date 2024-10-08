from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

def contact(request):
    return render(request, "contact.html")

def store_contact(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        message = request.GET.get('message')
        
        Contact.objects.create(name=name, email=email, message=message)

        return HttpResponse('Congrats! Your message has been sent.')
    else:
        return HttpResponse('Invalid request method.', status=405)
