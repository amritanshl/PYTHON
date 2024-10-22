from django.shortcuts import render
import datetime


names = ['Amrit', 'sherina', 'Shweta','Pritam']
# Create your views here.
def home(request):
    return render(request, 'home.html',{'names':names})