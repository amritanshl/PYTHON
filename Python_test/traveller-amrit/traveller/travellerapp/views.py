from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dest1= Destination()
    dest1.name = "Himachal"
    dest1.desc = "Land of gods"
    dest1.price = 200
    dest1.img = "news_3.jpg"
    dest1.offer = True

    dest2= Destination()
    dest2.name = "Lakshadeep"
    dest2.desc = "Mini maldives"
    dest2.price = 1000
    dest2.img = "latest_3.jpg"
    dest2.offer= False

    dest3= Destination()
    dest3.name = "Jaipur"
    dest3.desc = "pinkcity"
    dest3.price = 300
    dest3.img = "news_1.jpg"
    dest2.offer = False

    dest3= Destination()
    dest3.name = "Jaipur"
    dest3.desc = "pinkcity"
    dest3.price = 300
    dest3.img = "news_1.jpg"
    dest2.offer = False


    dest = [dest1,dest2,dest3]



    return render(request, 'index.html', {'dest': dest})