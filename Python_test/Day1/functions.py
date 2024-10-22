import cmath
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