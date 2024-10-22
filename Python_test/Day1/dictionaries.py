capitals ={ "India":"New Delhi", "Crotia":"Zagreb","Russia": "Moscow","Russia":"Chennai","Itay":"Rome", "USA":"Washingtond DC","Russia": "Avdivkaa"}
print(capitals)

cities = {"India":["Bengaluru", "New Delhi"], "USA":["New York", "Washington"], "Russia":["Cremia","Pittsburg", "Moscow"]}

cities_and_countries = capitals | cities
#print(cities_and_countries)



capitals['India'] = 'Chennai'
#print(capitals)

#print(cities['Russia'][-1])

mybio = {
    'fname':'Amritansh',
    'lname':'Lal',
    'age':27,
    'country':'India',
    'isMarried': False,
    'skills': ['MS Azure', 'Databricks','Plwershell', 'Python'],
    'street':'Whitefileds',
    'address2':{
        'permanent address' :{
            'City': 'Ghaziabad',
            'state': 'Uttar Pradesh',
            'zipcode':201017,
            'phone':[9999558384,88888888,555555]
        },
        'present Address':{
            'City': 'Bengaluru',
            'state': 'Karnataka',
            'zipcode':301525,
            'phone':88888
        }
            

    }
}

mybio1 = {
    'fname':'Pritam',
    'lname':'Sengupta',
    'age':27,
    'country':'USA',
    'isMarried': False,
    'skills': ['MS Azure', 'Databricks','Plwershell', 'Python'],
    'address1':{
        'permanent address' :{
            'City1': 'Ghaziabad',
            'state': 'Uttar Pradesh',
            'zipcode':201017,
            'phone':[9999558384,88888888,555555]
        }
       
            

    }
}

#mybio['address']['permanent address']['phone'][1] =852468541685 
#print(mybio['address']['permanent address']['phone'][1])

v = dict()
v = mybio.update(mybio1)
print(v)

#print(mybio.get("amrit"))
#print(mybio['amrit'])

#print(mybio.get('address'))

#print(mybio.keys())
#print(mybio.values())

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}

#for x in numbers: 
    #print(x,":", numbers[x])