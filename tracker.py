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

    @abstractmethod
    def category_wise_total(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass
    
    @abstractmethod 
    def delete_expense(self):
        pass


# -------- Concrete Class --------
class MyExpenseTracker(ExpenseTracker):

    def __init__(self):
        self.__expensesList = []
        self.file_name = "expenses.txt"
        self.load_from_file()   #  load old data at start

    # load from file
    def load_from_file(self):
        try:
            file = open(self.file_name, "r")
            for line in file:
                data = line.strip().split("|")

                if len(data) !=4:
                    continue   #skip wrong line
                expense = {
                    "date": data[0],
                    "category": data[1],
                    "description": data[2],   
                    "amount": float(data[3])
                }

                self.__expensesList.append(expense)

            file.close()
        except FileNotFoundError:
            pass   # first time run

    # save to file
    def save_to_file(self):
        file = open(self.file_name, "w")

        # write each expense as a line
        for expense in self.__expensesList:  
            line = f"{expense['date']}|{expense['category']}|{expense['description']}|{expense['amount']}\n"
            file.write(line)

        file.close()

    # show menu
    def show_menu(self):
        print("\n==== MENU ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Category-wise Total")
        print("5. Delete Expense")
        print("6. Exit")

    # add expense
    def add_expense(self):
        date = input("Enter the Date (YYYY-MM-DD): ")
        
        # predifined categories
        categories = ["Food", "Travel", "Shopping", "Bills", "Others"]
        print("Select Category from below: ")
        for i, cat in enumerate(categories, start=1):
            print(f"[i]. {cat}")
            

        category = input("Enter catgory name:")
        
        if category not in categories:
            print("Invalid category! Please choose from the list.")
            return 
        
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

        self.__expensesList.append(expense)
        self.save_to_file()   # save immediately
        print("Expense Added Successfully!")

    # view expenses
    def view_expenses(self):
        if not self.__expensesList:
            print("No Expenses Added Yet.")
            return

        print("\n===== Your Expenses =====")
        for i, expense in enumerate(self.__expensesList, start=1):
            print(f"{i}. Date: {expense['date']}, "
                  f"Category: {expense['category']}, "
                  f"Description: {expense['description']}, "
                  f"Amount: ₹{expense['amount']}")

    # total expense
    def total_expense(self):
        total = sum(exp["amount"] for exp in self.__expensesList)
        print("Total Kharcha is: ₹", total)

    #category wise total
    def category_wise_total(self):
        if not self.__expensesList:
            print("No expenses available.")
            return

        category_total = {}

        for expense in self.__expensesList:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        print("\n--- Category Wise Total ---")
        for cat, total in category_total.items():
            print(f"{cat} : ₹{total}")
    
    # Delete Expense
    def delete_expense(self):
        if not self.__expensesList:        
            print("no expenses to delete")
            return 
        
        # show all expenses
        self.view_expenses()

        try:
            choice = int(input("Enter expenses number to delete: "))
            index = choice - 1

            if index < 0 or index >= len(self.__expensesList):
                print("Invalid Expense number. ")
                return 
            
            confirm = input("Are you sure you want to delete this expense? (y/n): ")

            if confirm.lower() != 'y':
                print("Delete cancelled.")
                return
            
            deleted_expense = self.__expensesList.pop(index)
            
            self.save_to_file()
            print("Expense deleted successfully!")
            print(f"Deleted: {deleted_expense['category']} - ₹{deleted_expense['amount']}")
        except ValueError:
            print("Please enter a valid number.")


    # getter method to access private expenses list
    def get_expenses(self):
        return self.__expensesList
    
    # setter method to add expense with validation
    def add_expense_secure(self, expense):
        if expense["amount"] > 0:
            self.__expensesList.append(expense)
            self.save_to_file()
        else:
            print("Amount must be greater than zero")    
    
    
        
               
    
        
