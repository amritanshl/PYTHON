# #declare a function
# def myFunc():
#     print("Amritansh ")

# num1 = int(input("enter first number: "))
# num2  = int(input("enter second number: "))
# choice = input("""
# + for addition
# - for subtraction
# * for multiplication
# / for division                                            
# """)



# #functions with parameters
# def sum(num1, num2,*values):
#     a = 0
#     for x in values:
#         a=a+x
#     return print("Addition of numbers",a)

# def sub(num1 ,num2):
#     return  num1-num2

# def mul(num1=1 ,num2=1):
#     return print("Multiplication of numbers", num1*num2)

# def div(num1 ,num2=1):
#     return print("Division of numbers", num1/num2)

# sum = lambda num1, num2 : num1+num2
# dif = lambda num1, num2 : num1-num2
# mul = lambda num1, num2 : num1*num2
# div = lambda num1, num2 : num1/num2

# match choice:
#     case '+':
#         print(sum(num1,num2))
#     case '-':
#         dif(num1,num2)
        
#     case '*':
#         mul(num1,num2)
#     case '/':
#         div(num1,num2)



# num1 = int(input("Enter the number "))

# def find_prime_numbers(num1):
#     prime = []

#     for y in  range(2, num1//2+1):   
        
#             if num1%y  ==0:
#                 break
#             else:
#                 prime.append(y)
#     return prime
                
# print(find_prime_numbers(num1))
    


# num = 12
 
# for num in range(2, num + 1):

#    if num > 1:

#        for i in range(2, num):

#            if (num % i) == 0:

#                break

#        else:

#            print(num)



# def reverse_a_string (mystr):
#     reversedStr = ''

#     index = len(mystr)

#     while index>0:
#         reversedStr+=mystr[index-1]
#         index=index-1

#     return print(reversedStr)

# reverse_a_string("Amritansh")

# numbers = itemList=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# # keys = list(numbers.keys())
# # keys.sort()
# # sortit = {i : numbers[i] for i in keys}

# sortit = sorted(numbers, key=lambda x: x['amount'])
# print(sortit)




# def sum_function (*num):
#     total= 0 
#     #mylist = list(num)
#     for x in num:
#         total +=x
#     return print("Result ",total)

# listOfNum = []

# while True:
    
#     try:
#         num1 = int(input("num1 "))
#         listOfNum.append(num1)
#     except KeyboardInterrupt:
#         print('')
#         sum_function(*listOfNum)
#         break
        
    
































