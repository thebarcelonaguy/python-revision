import os
import art

clear = lambda: os.system('clear')
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def calculator():
    again=True
    print(art.logo)
    first_number=float(input("what is the first number?: "))
    while(again):
        print("+\n-\n*\n/\n")
        operation_input=input("Pick an operation: ")
        second_number=float(input("What's the next number?: "))
        dict1={"+":addition,"-":subtraction,"*":multiplication,"/":division}
        calculation_fxn=dict1[operation_input]
        result=calculation_fxn(first_number,second_number)
        print(f"{first_number} {operation_input} {second_number} = {result}")
        flag=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if(flag=="y"):
            first_number=result
        else:
            again=False
            clear()
            calculator()

calculator()   
