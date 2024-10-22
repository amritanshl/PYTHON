from datetime import datetime
class Person():
    def __init__(self,name, country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def calculate_age(self):
        current_year= datetime.now().year
        birth_date=datetime.strptime(self.dob, '%d/%m/%Y')
        age=str(current_year-birth_date.year-1)
        return self.name + "'s age is "+ age + ". He is residing in "+self.country
   
name = input("Enter the name: ")
country = input("Enter the country: ")
dob = input("Enter DOB (DD/MM/YYYY): ")
person_details = Person(name,country,dob)
print(person_details.calculate_age())