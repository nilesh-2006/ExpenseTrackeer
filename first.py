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
# a={1,4,3}
# b={3,4,5}
# print(a.difference(b))

#Login System (Username + Password Check) 
# correct_user="Nilesh"
# correct_pass="1234"

# while True:
#     user=input("Enter Username: ")
#     pas=input("Enter Password: ")
    
#     if user==correct_user and pas==correct_pass:
#         print("Login Successfully!")
#         break
    
#     else:
#         print("Invalid  Try Again!....\n")    

#print no 1 to 100
# num=1
# while num<=100:
#     print(num)
#     num=num+1

#sum of first 5 nos
# i=1
# sum=0
# while i<=5:
#     sum=sum+i
#     i=i+1
#     print(sum)
            
#Print even numbers from 2 to 20            
# num=2
# while num<=20:
#     if num%2==0:
#         print(num)
#         num=num+2

# number = 5

# while number >= 1:
#     print(number)
#     number -= 1

# i=1
# while i<=10:
#     print("2 x",i,"=",2*i)
#     i=i+1

#Student Marks Management
# total=0
# count=0

# while True:
#     marks=int(input("Enter marks (or -1 to stop): "))
    
#     if marks==-1:
#         break
#     total+=marks
#     count+=1
# avg=total/count
# print("Average marks:",avg)    

#Number Guessing Game

# import random

# secret = random.randint(1, 20)

# guess = 0

# while guess != secret:
#     guess = int(input("Guess the number (1-20): "))

#     if guess < secret:
#         print("Too Low!")
#     elif guess > secret:
#         print("Too High!")
#     else:
#         print("Correct! You win!")


#Functions
# def my_function():
#     a=10
#     b=22
#     sum=a+b
#     print(sum)
#     avg= (a+b)/2
#     print(avg)
    
# my_function()  
# def cal_per(total,obtained):
#     percent=(obtained/total)*100
#     return percent

# p= cal_per(500,430)
# print("percentage =",p)

# def add(a,b):
#     print("sum=", a+b)
    
# add(5,6) 

#function with return parameter
# def square(n):
#     return n*n
# result= square(7)
   
# print(result)

#Function to Check Even or Odd
# def Even_odd(n):
#     if n % 2 == 0:
#         print(n,"even no.")
#     else:
#         print(n,"odd no.")
# Even_odd(10)        
   
#    Function With Loop (Print Table) 
# def table(n):
#     for i in range(1,11):
#         print(n,"x",i, "=",n*i) 
# table(5)           

#Function Returning Multiple Values
# def calculate(a, b):
#     add = a + b
#     sub = a - b
#     return add, sub

# x, y = calculate(10, 3)
# print("Addition:", x)
# print("Subtraction:", y)

#Function With Default Parameter
# def welcome(name="Nilesh"):
#     print("Welcome",name)
# welcome()    
# welcome("Atul")            
       
# def student(name, course="BCA"):
#     print("Name:", name)
#     print("Course:", course)

# student("Nilesh")
# student("Atul", "B.Tech")

# def total_sum(numbers):
#     return sum(numbers)

# print(total_sum([10, 20, 30, 40]))

# def is_adult(age):
#     return age >= 18

# print(is_adult(15))
# print(is_adult(21))

#Function Using String Operations
# def count_vowels(text):
#     vowels="aeiouAEIOU"
#     count=0
#     for ch in text:
#         if ch in vowels:
#             count+=1
#     return count

# print(count_vowels("python programming"))

# def fun(animal, name):
#     print("I have a ",animal)
#     print("my ", animal+" name is ",name) 
# fun("buddy", "dog")    
           
# Sending a list as an argument        
# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit) 

# my_fruits=["apple", "banana", "cherry"]
# my_function(my_fruits)

#Sending a dictionary as an argument:
# def my_fun(person):
#     print("Name:", person["name"])   
#     print("Age", person["age"])
    
# my_per={"name":"nilesh", "age":19}    
# my_fun(my_per)

#A function that returns a list:
# def my_function():
#   return ["apple", "banana", "cherry"]

# fruits = my_function()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

#A function that returns a tuple
# def my_function():
#     return (10,20)

# x,y= my_function()
# print("x:", x)
# print("y:", y)

# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")

