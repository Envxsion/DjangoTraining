from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'General Chat'},
    {'id':2, 'name':'Front end devs'},
    {'id':1, 'name':'Python Only'},
]

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')