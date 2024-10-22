# class cars:
#     def __init__(self,brand="Mercedes", engine="Electric", power=200, typeoFCar="Hatchback"):
#         self.brand = brand
#         self.engine = engine
#         self.power = power
#         self.typeoFCar = typeoFCar
#     def _del_(self) :
#         print("Delete everything ")
#     def car_info(self):
#         return f'I have a {self.brand}, which produces {self.power} BHP. It is a {self.typeoFCar} with {self.engine} engine '
    
        

# c = cars()
# print(c.car_info())

# print(cars("BMW", "IC", 500, "Sedan").car_info())

# print(c.power)
# print(c.engine)
# print(c.brand)
# print(c.typeoFCar)


# class calc:
#     a =1 
#     b = 2
#     def __init__(self,num1, num2):
#         self.a = num1
#         self.b = num2
#     def addition(self):
#         return print(self.a+self.b)
#     def multiplication(self):
#         return print(self.a*self.b)

# c = calc(10,2)
# c.addition()
# c.multiplication()

#Write a Python program to create an instance of a specified class and display the namespace of the said instance.


#base Class
# class cars(object):
#     def __init__(self,country ):
#         self._brand = "BMW"
#         self.country = country

#     # def printBrand(self):
#     #     print(self.brand) 

# #derived Class    
# class model(cars): 
#     def __init__(self, brand,country, modelofCar):
#         self.models = modelofCar
#         cars.__init__(self, country)
#         self._brand = "Audi"
        
#     #cars.printBrand()
        
#     def displayModel(self):
#         print(self.brand,"__ ",self.country,"___",self.models)

# carDetails  = model("BMW","Germany", "5 Series")

# #carDetails.printBrand()
# carDetails.displayModel()
    







