
# # Introduction
# # Day 1 - 30DaysOfPython Challenge

# print(2 + 3)   # addition(+)
# print(3 - 1)   # subtraction(-)
# print(2 * 3)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)

# # Checking data types

# print(type(10))                  # Int
# print(type(3.14))                # Float
# print(type(1 + 3j))              # Complex
# print(type('Amrit'))          # String
# print(type([1, 2, 3]))           # List
# print(type({'name':'Amrit'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple



# # Variables in Python
# first_name = 'Amrit'
# last_name = 'Lal'
# country = 'Finland'
# city = 'Helsinki'
# age = 25
# is_married = False
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Amrit',
#    'lastname':'Lal',
#    'country':'Finland',
#    'city':'Helsinki'
#    }

# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

myval = "jitin singh ajay"
def firstU(myval):
    resStr = ""
    arr = myval.split(" ")
    for x in arr:
        resStr = resStr + x[0:1].upper() +x[1:len(x)]+ " "
    return print(resStr)
# firstU(myval)


a = lambda y : y *2

print(a(5646))


