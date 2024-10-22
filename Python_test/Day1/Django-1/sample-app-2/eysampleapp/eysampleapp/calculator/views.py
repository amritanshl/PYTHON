from django.shortcuts import render

# Create your views here.
def calculator (request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    return render(request, "results.html",{'result':result})