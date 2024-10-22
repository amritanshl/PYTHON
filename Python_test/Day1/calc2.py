num1 = int(input("Enter first agni pareekshar: "))
num2 = int(input("Enter second agni pareekha: "))
choice = input("""
    + for addition
    - for subtraction
    / for division
    * for multiplication 
    Vibe ni aari to cheater bol do                 

""")
exitcon = ""
while(exitcon != "Cheater"): 
    match choice:
        case '+':
            print(num1+num2)
        case '-':
            print(num1-num2)
        case '*':
            print(num1*num2)
        case '/':
            print(num1/num2)        