from django.shortcuts import render

rooms = [
  {"id":1, "name": "Lets learn python"},
  {"id":2, "name": "Start design"},
  {"id":3, "name": "FE Devs"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')