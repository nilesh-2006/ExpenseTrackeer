# -------- Main Program --------

from tracker import MyExpenseTracker

tracker = MyExpenseTracker()

print("***** Welcome to Expense Tracker *****")
while True:
    tracker.show_menu()

    try:
        choice = int(input("Please Enter your Choice: "))
    except ValueError:
        print("Invalid input!")
        continue

    if choice == 1:
        tracker.add_expense()
    elif choice == 2:
        tracker.view_expenses()
    elif choice == 3:
        tracker.total_expense()
    elif choice == 4:
        tracker.category_wise_total()
    elif choice == 5:
        tracker.delete_expense()
    elif choice == 6:
        print("Thank you for using Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid Choice.")
