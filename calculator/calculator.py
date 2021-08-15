choice="p"
def calculator(num1,num2,symbol):
    if symbol=="+":
        return num1+num2
    elif symbol=="-":
        return num1-num2
    elif symbol=="*":
        return num1*num2
    elif symbol=="/":
        return num1/num2
    


def calculation():
    num1=int(input("What is the first number? "))
    print(f"+\n-\n*\n/")
    symbol=input("choose an operation: ")
    num2=int(input("What is the second number? "))
    ans=calculator(num1,num2,symbol)
    print(f"{num1}{symbol}{num2} = {ans}")
    choice=input(f"Type \'y\' to continue calculating with {ans},or type \'n\' to start a new caluculation or q to Quit ")
    if choice=="y":
        calculation2(ans)
    elif choice=="n":
        calculation()
    elif choice=="q":
        print("bye bye")
    
    
def calculation2(num1):
    print(f"+\n-\n*\n/")
    symbol=input("choose an operation: ")
    num2=int(input("What is the second number? "))
    ans=calculator(num1,num2,symbol)
    print(f"{num1}{symbol}{num2} = {ans}")
    choice=input(f"Type \'y\' to continue calculating with {ans},or type \'n\' to start a new caluculation or q to Quit ")
    if choice=="y":
        calculation2(ans)
    elif choice=="n":
        calculation()
    elif choice=="q":
        print("bye bye")
if choice=="p":
    calculation()

