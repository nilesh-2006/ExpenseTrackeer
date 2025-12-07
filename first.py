# students = ["Rahul", "Nilesh", "Priya", "Atul"]

# for name in students:
#     print("Message sent to", name)

#Shopping list check karna
# items=["Milks","bags","eggs"]
# for item in items:
#     print(item)

# Students ko message bhejna 
# Students=["Nilesh","Atul","Kajal"]
# for s in Students:
#     print("hello",s,"you are selected for the team ")

# ! se 10 tak counting
# for i in range(1,11):
#     print(i)

#Movie ke har character ko print karna 
# name= "MOVIE"
# for ch in name:
#     print(ch)

#Expenses ka total 
# expenses=[500,200,300]
# total=0
# for amount in expenses:
#     total= total+amount
# print("Total Expenses is:",total)

# check even numbers from 1 to 20 
# for i in range(1,21):
#     if i%2==0:
#         print(i, " is even") 
#     else:
#         print(i, "id odd")   

#Multiplication table
# num = 5
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

#Average marks
# marks = [10, 20, 30]
# total = 0
# for m in marks:
#     total += m
# print(total/len(marks))
    
#Range with step
# for i in range(2, 21, 2):
#     print(i)

#break Statement
#Searching a contact

# contacts = ["Nilesh", "Rahul", "Atul", "Priya"]

# for name in contacts:
#     if name == "Atul":
#         print("Contact Found:", name)
#         break   # loop yahi ruk jayega
#     print("Checking:", name)

#ATM — wrong PIN 3 attempts
# pins=[1111,2222,3333]
# correct_pin=2222
# for p in pins:
#     if p==correct_pin:
#         print("login successful")
#         break
    
#     print("wrong pin:",p)

#Online shopping — stop when item out of stock

# stocks = [10, 5, 0, 7, 9]

# for s in stocks:
#     if s == 7:
#         print("Item Out of Stock! Stopping checking…")
#         break
#     print("Stock available:", s)

# continue Statement
#   Attendance system 

# students = ["Nilesh", "Absent", "Atul", "Priya"]

# for s in students:
#     if s == "Absent":
#         continue   # isko skip kar do
#     print("Sending message to:", s)
 
#Bank transaction — skip ₹0 transactions
# transactions = [200, 0, 500, 0, 150]

# for t in transactions:
#     if t == 0:
#         continue  # 0 amount skip
#     print("Processing transaction:", t)


# marks = [50, -1, 60, 72, -1]

# for m in marks:
#     if m < 0:
#         continue   # invalid marks skip
#     print("Valid mark:", m)
 
# for i in range(5):
#     if i == 3:
#         pass   # is par kuch mat karo
#     else:
#         print("Value:", i)

# Basic Square Star Pattern 
# for i in range(4):
#     for j in range(4):
#         print("*", end="  ")
#     print()    

#Basic Square Star Pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#Dict
# ------------------------------
#   Complete Dictionary Program
# ------------------------------

# 1. Creating a Dictionary
# student = {
#     "name": "Nilesh",
#     "age": 21,
#     "course": "BCA",
#     "city": "Nagpur"
# }

# print("\nOriginal Dictionary:")
# print(student)


# # 2. Accessing values using key
# print("\nName:", student["name"])

# 3. Accessing using get()
# print("City:", student.get("city"))

# # 4. keys() method
# print("\nAll Keys:")
# print(student.keys())

# # 5. values() method
# print("\nAll Values:")
# print(student.values())

# # 6. items() method
# print("\nAll Items (key-value pairs):")
# print(student.items())

# # 7. Adding a new item
# student["email"] = "nilesh123@gmail.com"
# print("\nAfter Adding Email:")
# print(student)

# # 8. Updating value using assignment
# student["age"] = 22
# print("\nAfter Updating Age:")
# print(student)

# # 9. update() method -> multiple updates
# student.update({"city": "Pune", "phone": "9876543210"})
# print("\nAfter update() Method:")
# print(student)

# # 10. pop() method -> remove by key
# removed = student.pop("phone")
# print("\nAfter pop('phone'), removed =", removed)
# print(student)

# # 11. popitem() -> removes last item
# last_removed = student.popitem()
# print("\nAfter popitem(), removed =", last_removed)
# print(student)

# # 12. setdefault() -> get value or create new key
# student.setdefault("gender", "Male")
# print("\nAfter setdefault('gender'):")
# print(student)

# # 13. Copy dictionary
# student_copy = student.copy()
# print("\nCopied Dictionary:")
# print(student_copy)

# # 14. fromkeys() -> create new dictionary with default values
# subjects = ("math", "science", "english")
# default_marks = 0
# marks = dict.fromkeys(subjects, default_marks)

# print("\nDictionary Using fromkeys():")
# print(marks)

# # 15. clear() -> empty dictionary
# student.clear()
# print("\nAfter clear(), student dictionary becomes:")
# print(student)

# marks={
#     "math":90,
#     "science":86,
#     "english":88
# }
# print(marks)

#Sets in python 
# A set is a collection of unordered and unique itmes. sets automatically remove duplicate elements and are written using curly braces {}
# languages={"python","java","c","python","c++"}


# #Adding item to a set
# languages.add("c++")
# print(languages)
# #Removing item 
# languages.remove("java")
# print(languages)
# #  sets do not entertain duplicacy
# discard() Removes item; no error if not found 
# languages.discard("ruby")
# print(languages)
# pop() Removes random element 
# languages.pop()
# print(languages)

# numbers = {10, 20, 30, 40, 50}

# removed_item = numbers.pop()

# print("Removed Item:", removed_item)
# print("Remaining Set:", numbers)

#union() 
a={1,4,3}
b={3,4,5}
print(a.difference(b))