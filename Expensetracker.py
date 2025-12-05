#Expense Traker Project 

expensesList=[]  # List of expenses in form of dictionary
print("*****Welcome TO Exxpense Tracker*****")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3.View Total Expenses")
    print("4. Exit")
    
    choice=int(input("Please Enter your Choice: "))
    
#Add Expense    
    if(choice==1):
        date=input("Enter the Date : ")
        category=input("Enter the Category (e.g., Food, Travel, Shopping): ")
        description=input("Enter Description: ")
        amount=float(input("Enter the Amount: "))
        
        expense={
            "date":date,
            "category":category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print(" \n Expenses is Added Successfully")

# 2. View All Expenses 
    elif(choice==2):
        if( len(expensesList)==0):
            print("No Expenses Added. ")
        else:
            print("===== Your Expenses====")    
            count=1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count}-> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]}")
                count= count+1

#3. View Total Expenses
    elif(choice==3):
        total=0
        for eachKharcha in expensesList:
            total=total + eachKharcha["amount"]
            print("\n Total Kharcha is:",total)

# 4. Exit
    elif(choice==4):
        print("Thank you for using Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid Choice. please try agrain ")
    
    
                   
            
                            
                   
        