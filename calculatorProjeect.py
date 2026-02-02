import math

calculation=True
 
while calculation:
    num1=float(input("Enter the first number: "))
    
    oprator=input("Enter the opratoion you want to perform (+,-,*,/): ")

    num2=float(input("Enter the seconnd number: "))

    if oprator=="+":
        print(f"{num1} + {num2} =",num1+num2)
        
    elif oprator == "-":
        print(f"{num1} - {num2} =",num1-num2)
        
    elif oprator == "*":
        print(f"{num1} * {num2} =",num1*num2)
        
    elif oprator == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")
        
    else :
        print("Invalid oprator!!!!")
    
    user_choice=input("you want to continue calculation Y/N: ").upper()
    
    if user_choice=="N": 
        calculation=False
    
print("\n calculator closed.....Thank you")