from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  # return HttpResponse("<h1>hi</h1>")
  return render (request,"index.html")

# def contact(request):
#   return render(request, "contact.html")
  
