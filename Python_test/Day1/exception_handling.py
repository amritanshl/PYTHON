


# try:
#     num1 = int(input("enter first number: ")) # not add interger value- Value Error
#     num2  = int(input("enter second number: "))
#     choice = input("""
# + for addition
# - for subtraction
# * for multiplication
# / for division                                            
# """)
    
#     def sum(num1, num2):
    
#         return print("Addition of numbers ",num1+num2)

#     def sub(num1 ,num2):
#         return  print("Subtraction of numbers, ",num1-num2)

#     def mul(num1 ,num2):
#         return print("Multiplication of numbers ", num1*num2)

#     def div(num1 ,num2):
#         try:
#             return print("Division of numbers ", num1/num2)
#         except ZeroDivisionError:
#             return print("Zero is not allowed in division ", str(Exception))

#     div(num1,num2) #don't provide either num1 or num2 then it'll be Name Error

# except (NameError, ValueError):
#     print("Exception occured ")

# myList = ['a','b','c']
# try: 
#     print(myList[3])
# except IndexError:
#     print("This number is out of range ")

# print("It still works")
# try: 
#     import azure as az 
# except ModuleNotFoundError:
#     print("Module doesn't exist ")

#functions with parameters


try:
    print( 50/0)
except Exception as e:
    print(e)




