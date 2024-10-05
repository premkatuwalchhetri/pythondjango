from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  # return HttpResponse("<h1>hi</h1>")
  return render (request,"index.html")

def contact(request):
  return HttpResponse("""
                      <title>CONTACT</title>
                      <button>9742516921</button>
                      <a>Feel freee to contact us</a>""")