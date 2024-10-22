from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method=='POST':
        num1 = request.method.GET['num1']
        num2 = request.method.GET['num2']
        add = request.method.GET['add']
        sub = request.method.GET['sub']
        mul = request.method.GET['mul']
        div = request.method.GET['div']
        choices = [add,sub,mul,div]

        if request.method.POST['add'] != None: