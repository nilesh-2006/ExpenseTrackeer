# Expense Tracker Project

expensesList = []  # List of expenses in form of dictionary

print("***** Welcome to Expense Tracker *****")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    try:
        choice = int(input("Please Enter your Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # 1. Add Expense
    if choice == 1:
        date = input("Enter the Date: ")
        category = input("Enter the Category (e.g., Food, Travel, Shopping): ")
        description = input("Enter Description: ")
        
        try:
            amount = float(input("Enter the Amount: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nExpense Added Successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added Yet.")
        else:
            print("\n===== Your Expenses =====")
            count = 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> Date: {eachKharcha['date']}, "
                      f"Category: {eachKharcha['category']}, "
                      f"Description: {eachKharcha['description']}, "
                      f"Amount: ₹{eachKharcha['amount']}")
                count += 1

    # 3. View Total Expenses
    elif choice == 3:
        total = 0
        for eachKharcha in expensesList:
            total += eachKharcha["amount"]

        print("\nTotal Kharcha is: ₹", total)

    # 4. Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid Choice. Please try again.")
