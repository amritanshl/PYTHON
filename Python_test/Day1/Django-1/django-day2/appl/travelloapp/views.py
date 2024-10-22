from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):

    dest =  Destination()
    dest.name = "Lakshadweep"
    dest.price = 500
    dest.desc = "Maldives of India"
    dest.img = 'destination_9.jpg'




    return render(request, 'index.html',{'dest': dest})