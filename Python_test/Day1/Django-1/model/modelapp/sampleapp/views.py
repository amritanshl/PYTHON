from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):

    empdt3 = Employee()    
    empdt3.name = "amritansh"
    empdt3.dept="IT"
    empdt3.phone=9999558384
    empdt3.salary = 1000000

    empdt1 = Employee()    
    empdt1.name = "shweta"
    empdt1.dept="finance"
    empdt1.phone=88888888
    empdt1.salary = 1500454

    empdt2 = Employee()    
    empdt2.name = "Pritam"
    empdt2.dept="Accounts"
    empdt2.phone=777777
    empdt2.salary = 250000

    empdt = [empdt1, empdt2, empdt3]


    return render(request, "index.html", {'empdt': empdt})