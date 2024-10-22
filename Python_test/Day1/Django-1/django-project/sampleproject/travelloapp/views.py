from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dests = Destination.objects.all()


    return render(request, 'index.html', {'dests':dests} )
#     dest1 = Destination()
#     dest1.name = "Lakshadweep"
#     dest1.description ="Maldives of India"
#     dest1.img ="destination_5.jpg"
#     dest1.price = 1000
#     if dest1.price<1000:

#         dest1.offer = True
#     else:
#         dest1.offer = False


#     dest2 = Destination()
#     dest2.name = "Rajasthan"
#     dest2.description ="Thar desert is here"
#     dest2.img ="destination_6.jpg"
#     dest2.price = 700
#     if dest2.price<1000:

#         dest2.offer = True
#     else:
#         dest2.offer = False
   

#     dest3 = Destination()
#     dest3.name = "Himachal Pradesh"
#     dest3.description ="Top of the India"
#     dest3.img ="destination_2.jpg"
#     dest3.price = 500
#     if dest3.price<1000:

#         dest3.offer = True
#     else:
#         dest3.offer = False
    

#     dests = [dest1,dest2,dest3]
    


    