# create empty list
myList = list()
print("emptyList: ",len(myList))

#empty list 2
list2 = []
print("emptyList: ",len(list2))

# Print the lists and its length
companies = ['ey', 'LnT','Accenture','HCL','Capgemini']

del companies

#Delete all the elements from the list
#companies.clear()

#Insert element at a particular index
#companies.insert(2,'JP Morgan Chase')

#remove a particular element based on name
#companies.remove('Capgemini')

#remove a paritcular element if we give index else remove last item from the list
#companies.pop(3)


print('Companies: ',companies)
print("Length of copmaines: ",len(companies))

#check if the company exists in the list
if('EY' in companies):
    print("EY exists")
else:
    print("EY does not exist")


#list with different data type
myBioLst = ['Amritansh', 'Lal', 27, False, {'country': 'India', 'city':'New Delhi'}, ['Mom', 'Dad','Brother'],'Rittik', 'EY']
#print(myBioLst[5][1])

# []List
# {}Set/Dictionary
# ()array

#join two list
companies_join_myBioList = companies + myBioLst
print(companies_join_myBioList)

#join by using extend command
myBioLst.extend(companies)
print(myBioLst)

#Find the index of element
indexOfAccenture = companies.index('Accenture')
print("Index of my comapny: ",indexOfAccenture)


#example for parsing datatyp inside a list
listOfString = []
for x in myBioLst:
    if(type(x) is str):
        listOfString.append(x.lower())
        
print(listOfString)
if('ey' in listOfString):
    print("EY exists")
else:
    print("EY doesn't exist")




#modify city in the list
myBioLst[4]['city']= 'Bengaluru'
#modify Last Name in the list
myBioLst[1] ="Sri"

#multi0variable assgnment or unpacking list
fname,lname,age,maritaStatus, address, familyMembers,*rest = myBioLst



print("First Name: ",fname)
print("Last Name: ",lname)
print("Age: ",age)
print("Marital Status: ",maritaStatus)
print("Country: ",address['country'])
print("City: ",address['city'])
print("Family Members: ",familyMembers)
print("Head of family: ",familyMembers[0])

#sorting
marks1 = [52,78,91,75,39,66,47,78,99,95,82,71]
marks2 = [52,'Amritansh', 'Lal', 27, False,45,91,75,8,66,47,78,354,95,345,71,'First Name']
marks3 = [54,78,91,34,39,66,47,354,345,95,'Head of family',82,71]
marks4 = [356,78,34,75,5,'Amritansh', 'Lal', 27, False,66,47,783,99,95,82,71]
marks5 = [877,78,91,75,354,'Amritansh', 'Lal', 27, False,66,34,78,543,95,345,71]
marks1.sort(reverse=True)
first, second, third, *rest = marks1
print("First Posittion: ", first)
print("Second Posittion: ", second)
print("Third Posittion: ", third)
print("Rest of the class : ", rest)

#sum of all items in a list(sum of all the marks)
sum_of_marks= 0
for y in marks1:
    sum_of_marks += y

print("Sum of all the marks", sum_of_marks)

firstThreeMembers = marks1[0:3]
print(firstThreeMembers)

lastThreeMembers = marks1[-4:-1]
print(lastThreeMembers)

lengthOfMyMarksList = len(marks1)
#alternativeforAscending = marks[-lengthOfMyMarksList]
#sprint(alternativeforAscending)


#Resuable function to get the sum of all the integer values in a list
def sumOfIntegersfunction(items):
   # print(len(items))
    listOfInteger = []
    for i in items:
        if(type(i) is int):
            listOfInteger.append(i)
    sum_of_items= 0
    for j in listOfInteger:
        sum_of_items += j   
    return sum_of_items 

#Resuable function to get the multiplication of all the integer values in a list
def multiplicationOfIntegersfunction(items):
   # print(len(items))
    listOfInteger = []
    for i in items:
        if(type(i) is int):
            listOfInteger.append(i)
    sum_of_items= 1
    for j in listOfInteger:
        sum_of_items *= j   
    return sum_of_items 

print(sumOfIntegersfunction(marks1))

print(sumOfIntegersfunction(marks2))

print(sumOfIntegersfunction(marks3))

print(sumOfIntegersfunction(marks4))

print(sumOfIntegersfunction(marks5))

print(multiplicationOfIntegersfunction(marks1))

print(multiplicationOfIntegersfunction(marks2))

print(multiplicationOfIntegersfunction(marks3))

print(multiplicationOfIntegersfunction(marks4))

print(multiplicationOfIntegersfunction(marks5))

empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 





import schedule 
import time 
import os
import datetime
import sys
 

def job():
    #get_currentDirectory = os.path.dirname(os.path.abspath()) 
    mode= 0o666
    current_time = datetime.datetime.now()
    year_f = str( datetime.datetime.now().year)
    month_f= str(datetime.datetime.now().month)
    day_f= str(datetime.datetime.now().day)
    hour_f= str(datetime.datetime.now().hour)
    min_f= str(datetime.datetime.now().minute)
    sec_f= str(datetime.datetime.now().second)
    print(current_time,year_f,month_f,day_f,hour_f,min_f,sec_f)
    get_currentDirectory = os.path.exists(os.path.join(os.getcwd(),'files','2024'))
    print(os.path.exists(os.path.join(os.getcwd(),'files',year_f)))
    if(os.path.exists(os.path.join(os.getcwd(),'files',year_f))):
        year_path = os.path.join('files',year_f)
        
    else:
        year_path = os.path.join('files',year_f)
        os.mkdir(year_path, mode)

    if(os.path.exists(os.path.join(os.getcwd(),year_path,month_f))):
        month_path = os.path.join(year_path,month_f)
    else:
        month_path = os.path.join(year_path,month_f)
        os.mkdir(month_path, mode)
    if(os.path.exists(os.path.join(os.getcwd(),month_path,sec_f))):
        second_path = os.path.join(month_path,sec_f)
    else:
        second_path = os.path.join(month_path,sec_f)
        os.mkdir(second_path, mode)
    
     
 
schedule.every(10).minutes.do(job) 
schedule.every().second.do(job) 
#schedule.every().day.at("10:30").do(job) 
 
while 1: 
    schedule.run_pending() 
    time.sleep(1) 