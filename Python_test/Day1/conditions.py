x = 10
val = int(input("Please enter a number "))
if(val>x):
    print(str(val)+" is greater than" , x)
elif(val==0):
    print(str(val)+" is not allowd")     
else:
     print(str(val)+" is less than" , x)

print(val," is a positive number") if val > 0 else print(val, " is a negative number")      

if val>0 or val%2==0:
    print("this is allowed")
elif val==0:
    print(val, " is not allowed because its a zero")
else:
    print(val, " is a negative number or odd")
    
import math
euation = input("enter the euation: ")
a1 = int(euation[0])
b1 = int(euation[5])
c1 = int(euation[-1])
a = a1
b = b1
c = c1
print(type(c))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a) 
print('The solution are {0} and {1}'.format(sol1,sol2)) 
dis_form = b * b - 4 * a * c  
sqrt_val = math.sqrt(abs(dis_form))  
if dis_form > 0:  
    print(" real and different roots ")  
    print((-b + sqrt_val) / (2 * a))  
    print((-b - sqrt_val) / (2 * a))  
elif dis_form == 0:  
    print(" real and same roots")  
    print(-b / (2 * a))  
else:  
    print("Complex Roots")  
    print(- b / (2 * a), " + i", sqrt_val)  
    print(- b / (2 * a), " - i", sqrt_val)