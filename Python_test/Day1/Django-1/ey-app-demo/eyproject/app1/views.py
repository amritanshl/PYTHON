from django.shortcuts import render
import datetime

# Create your views here.
def myfunc(request):
    return render(request, 'home.html',{'date': datetime.datetime.now()})

def add(request):
    num1 = int(input(request.POST["num1"]))
    num2 = int(input(request.POST['num2']))
    result = num1 +num2
    


    return render(request,"result.html", {'result': result})
