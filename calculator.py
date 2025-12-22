#Calculator

# 1. Creating functions for operations
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    #to avoid division by zero error
    if b==0:
        return "Error connot divide by zero."
    return a/b


#2. Main calculator loop
while True:
    print("\n *** Simple calculator***")
    
    #Taking numbers as input
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter second Number: "))

    print("Choose operation: +  -  *  /")
    op = input("Enter operation: ")
    
    # 3. Deciding which function to call
    if op=="+":
        result= add(num1,num2)
    elif op=="-" :
        result= sub(num1,num2)
    elif op=="*":
        result= mul(num1,num2)       
    elif op=="/":
        result= div(num1,num2)
    else:
        print("Invalid operation selected")
    
    #showing output
    print("Result: ",result)
    
    # 4. Asking user if they want to continue
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break
    
                