typeOfFile = input("ASCII, UTF-16, UTF-8")

try: 
    with open( 'new.txt', 'r',encoding=typeOfFile) as file:
        file_data = file.read()
        print(file_data)
except UnicodeDecodeError:
    print("Code is wrong!! ")