from abc import ABC, abstractmethod

class ExpenseTracker(ABC):

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def add_expense(self):
        pass

    @abstractmethod
    def view_expenses(self):
        pass

    @abstractmethod
    def total_expense(self):
        pass

# -------- Abstraction Functions --------
class MyExpenseTracker(ExpenseTracker):

    def __init__(self):
        self.expensesList = []

    def show_menu(self):
        print("\n==== MENU ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

    def add_expense(self):
        date = input("Enter the Date: ")
        category = input("Enter the Category (Food, Travel, Shopping): ")
        description = input("Enter Description: ")

        try:
            amount = float(input("Enter the Amount: "))
        except ValueError:
            print("Invalid amount!")
            return

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        self.expensesList.append(expense)
        print("Expense Added Successfully!")

    def view_expenses(self):
        if not self.expensesList:
            print("No Expenses Added Yet.")
            return

        print("\n===== Your Expenses =====")
        for i, expense in enumerate(self.expensesList, start=1):
            print(f"{i}. Date: {expense['date']}, "
                  f"Category: {expense['category']}, "
                  f"Description: {expense['description']}, "
                  f"Amount: ₹{expense['amount']}")

    def total_expense(self):
        total = sum(exp["amount"] for exp in self.expensesList)
        print("Total Kharcha is: ₹", total)

    # -------- Main Program --------

   
