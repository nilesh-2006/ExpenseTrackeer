# 1. Write a function that prints “Hello Python” 5 times 

# def fun():
#     for i in range(5):
#         print("hello python")
# fun()   

# 2. Write a function that takes a name as input and prints a greeting message.

# def my_function(name):
#     print("hello",name,"welcome!")
    
# username=input("enter you name:")
# my_function(username)

# 3. Create a function that adds two numbers and prints the result

# def add(a,b):
#     result= a+b
#     print("sum=", result)
# add(2,4)   

# 4. Write a function that returns the square of a number.
 
# def square(n):
#     return n*n

# result= square(5)
# print("Square=" ,result)

# 5. Write a function to check whether a number is even or odd. 

# def evenodd(num):
#     if num%2==0:
#         print(num, "even number")
#     else:
#         print(num, "odd number") 
# n=int(input("enter number: "))
# evenodd(n)           

# 6. Write a function that prints the multiplication table of a given number. 

# def mul(num):
#     for i in range(1,11):
#         print(num, "x" ,i, "=", num*i)
# mul(5)        

# 7. Write a function to find the maximum of three numbers.

# print("\t \t  finding the largest of three number : ")
# x=int(input("Enter value of x:"))   
# y=int(input("Enter value of y:"))   
# z=int(input("Enter value of z:"))   
# def largest_no(x,y,z):
#     if (x>=y and x>=z):
#         print("x is largest")
#     elif(y>=x and y>=z):
#         print("y is largest")    
#     else:
#         print("c is largest")

# largest_no(x,y,z)        

# 8. Write a function that returns the sum of all numbers in a list.

# def my_function(numbers):
#     total=0
#     for i in numbers:
#         total+=i
#     return total

# my_list =[5,10,15,20]
# result= my_function(my_list)    
# print("sum of all numbers:", result)

# 9. Write a function to count how many vowels are in a string. 

# def count_vowels(text):
#     vowels= "aeiouAEIOU"
#     count=0
#     for char in text:
#         if char in vowels:
#             count=count+1
#     return count

# my_string= "Hello Nilesh"
# vowel_count= count_vowels(my_string)        
# print("number of vowels:", vowel_count)

# 10. Create a function that reverses a string.
# def reverse_string(text):
#     return text[::-1] #slicing to reverse

# my_string= "python"
# reversed_str=reverse_string(my_string)
# print("Reverse string is : ",reversed_str)

#OR

#Alternative method using a loop:
# def reverse_str(text):
#     reversed_text= ""
#     for char in text:
#         reversed_text=char + reversed_text
#     return reversed_text

# print(reverse_str("python"))    

# find factorial numbers 

# num=int(input("enter a no. to find factorial : "))
# def factorial(n):
#     result=1
#     for i in range(1, n+1):
#         result=result*i
#     return result

# print(f"Factorial of {num} is {factorial(num)}")    

#Python *args and **kwargs
'''1 *args (Arbitrary Positional Arguments)'''
# 1. *args allows a function to accept any number of positional arguments (0, 1, 2, …).

# 2. Inside the function, args behaves like a tuple. 
#Sum of any numbers

# def add_num(*args):
#     total=0
#     for num in args:
#         total=total+num
#     return total

# print(add_num(2,4,5))

# Print all names
# def greet(*names):
#     for char in names:
#         print("hello", char)

# greet("nilesh", "atul", " kajal")

# '''2. **kwargs (Arbitrary Keyword Arguments)  '''      
# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# student_info(name="Nilesh", age=19, city="Nagpur")
        
 # Scope of variable
 #1. Local variable 
# def outer():
#     x = 100  # Local variable
#     print(x)
# outer()

#2. Global variabl
# name="nilesh"
# def fun():
#     print(name)
# fun() 
# print(name)   

#Understanding the LEGB rule:
# x="global"
# def outer():
#     x="enclosing"
#     def inner():
#         x="local"
#         print("inner:",x)
#     inner()
#     print("outer:",x)

# outer()
# print("global:",x)   


# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
  
#   myfunc2()
#   return x

# print(myfunc1()  )

# def outer():
#     name="nilesh"
#     def inner():
#         name="kaju"
#         print("inner value:",name)
#     inner()
#     print("outer value:",name)
# outer()
    


# def outer():
#     x = 50
#     def inner():
#         x = 10
#         print(x)
#     inner()
#     print(x)

# outer()
# print(x)

# Global variable
# pi = 3.14

# def circle_area(radius):
#     # Local variable
#     pi = 3.14159
#     area = pi * radius * radius
#     return area

# # Taking radius from user
# r = float(input("Enter radius of circle: "))

# result = circle_area(r)

# print("Global pi =", pi)
# print("Area using LOCAL pi =", result)

# Decorator
# def decorator_function(fun):
#     def wrapper():
#         print("before the function runs...")
#         fun()
#         print("after the function runs...")
#     return wrapper

# @decorator_function
# def say_hello():
#     print("hello")
# say_hello() 

#Lmabda function 

#A lambda function in Python is a small, anonymous function defined using the lambda keyword.
#It can take any number of arguments but contains only one expression, which is automatically returned.
#Lambda functions are mainly used for short, simple operations and are often used with functions like map(), filter(), and sorted().

# add two no
# add= lambda a,b: a+b
# print(add(5,6))   
      
#Square of a number 
# square= lambda n: n*n
# print(square(5))     

#check even or odd
# is_even= lambda n: "Even" if n%2==0 else "odd"
# print(is_even(10))
# print(is_even(11))
      
#Lambda inside another function
# def my_fun():
#     return lambda a: a * 10
# result=my_fun()
# print(result(5))

#Function returns a lambda (Multiply by any number)
# def make_multiplier(n):
#     # lambda function created inside parent function
#     return lambda x: x * n

# double = make_multiplier(2)   # x * 2
# triple = make_multiplier(3)   # x * 3

# print(double(10))   # 20
# print(triple(10))   # 30

# num=[11,20,31,54,26,33,44,55,66,77,100]
# even= list(filter(lambda x: x%2==0 , num))
# print("even no",even)

#Re cursion
# Factorial using Recursion 
#formula of factorial
# n! =n*(n-1)!

# def factorial(n):
#     #base case
#     if n==1:
#         return 1
    
#     #recursive case 
#     else:
#         return n* factorial(n-1)


# print(factorial(5))

#A simple recursive function that counts down from 5:
# def countdown(n):
#     if n<=0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n-1)    

# countdown(5)

#fibonacci
# Function to return nth Fibonacci number using recursion
# def fibonacci(n):
#     if n<=1:
#         return n 
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)

# print(fibonacci(7))     


# def fibonacci(n):
#     # Base Case: agar n 0 ya 1 ho to directly return kar do
#     if n <= 1:
#         return n
#     else:
#         # Recursive Case: formula apply
#         return fibonacci(n - 1) + fibonacci(n - 2)


# # --- MAIN PROGRAM WITH USER INPUT ---
# num = int(input("Enter a number: "))

# result = fibonacci(num)
# print("Fibonacci number at position", num, "is:", result)
 
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# num = int(input("Enter a number: "))
# print("Factorial =", factorial(num))

#Create a function that returns the square of a number. 
# def function(n):
#     return n*n
# num=int(input("Enter a number: "))
# result=function(num)
# print("square=", result)

#Create a function that checks whether a number is even or odd.
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"

# # user input
# n = int(input("Enter a number: "))

# result = check_even_odd(n)
# print(result)

# #Create a function that takes 2 numbers and prints the larger one
# def larger(a,b):
#     if a>b:
#         print("Larger no. is: ",a)
#     elif b>a:
#         print("Larger no is : ",b)
#     else:
#         print("Both nos are equal")   

# num1=int(input("Enter Number 1:"))  
# num2=int(input("Enter number2: "))
# larger(num1,num2)           

# Write a function that converts Celsius → Fahrenheit
# def celsius_to_fehre(c):
#     f=(c * 10/5)+32
#     return f
    
# #input from user
# celsius=float(input("Enter temp in celsius: "))
# fehremheit = celsius_to_fehre(celsius)
# print(fehremheit) 

# Create a function that prints your name 5 times. 
# def myfun(name):
    
#     for i in range(5):
#         print(name)
        
# your_name= input("enter your name:")
# myfun(your_name)               
        
#Create a function that takes a string and returns its length.  
# def length_string(text):
#     count=0
#     for cha in text:
#         count+=1
#     return count

# user_string=input("Enter the string: ")
# result= length_string(user_string)
# print("Length of the string: ", result)

#Create a function that returns the cube of a number. 
# def cube(n):
#     return n**3

# num=int(input("Enter a number:"))
# result= cube(num)
# print(result)
   
#Function to check if a number is positive, negative, or zero. 

# def positive(num):
    
#     if num>0:
#         return  "is a positive."
#     elif num<0:
#         return "is a negative."       
#     else:
#         return  "is zero."

# n=int(input("enter a number: "))            
# result= positive(n)
# print("Result : ", result)

#Write a function that takes 3 numbers and returns their average.
# def Average(a,b,c):
#     avg= (a+b+c)/3
#     return avg

# x=float(input("Enter first number: "))
# y=float(input("Enter second Number: "))
# z=float(input("enter Third Number: "))

# result= Average(x,y,z)
# print("Average =", result)

#Create a function that returns the absolute value of a number 
# def abs(num):
#     if num < 0:
#         return -num
#     else:
#         return num
# n=float(input("Enter a no.:")  )
# result= abs(n)
# print("result:", result)  

# Function that counts vowels in a string. 
# def vowels_count(num):
#     vowels="aeiouAEIOU"
#     count=0
#     for i in num:
#         if i in vowels:
#           count+=1
#     return count

# n=input("Enter a String: ")
# result=vowels_count(n)     
# print("Vowels is :", result)
            
# Function that counts vowels and consonant in a string. 

# def count_vowels_consonant(text):
#     vowels= "aeiouAEIOU"
#     count_vowels=0
#     consonant_count=0
    
#     for cha in text:
#         if cha.isalpha():  # count the A-Z letters
#             if cha in vowels:
#                 count_vowels+=1
#             else:
#                 consonant_count+=1
#     return count_vowels , consonant_count

# s= input("Enter a String : ") 
# count_vowels , consonant_count = count_vowels_consonant(s)
# print("Total vowels: ",count_vowels)
# print("Total consonant: ", consonant_count)

#   Function that removes spaces from a sentence. 
# def remove_space(sentence):
#     result=""             
#     for char in sentence:
#         if char !=" ":
#             result+=char
#     return result

# s=input("Enter a string:")
# output= remove_space(s)
# print("sentence without spaces:", output)
               
#Function that checks if a number is prime.
# def prime(num):
#     if num<=1:
#         return "Not a prime number"

#     for i in range(2, int(num**0.5)+1):
#             if num%2==0:
#                 return "Not prime"

#     return "prime number"

# n=int(input("Enter a number:"))
# print(prime(n))

#factorial using loop
# def factorial(num):
#     fact=1
#     for i in range(1, num+1 ):
#         fact*=i
#     return fact

# n=int(input("Enter a number:"))
# result= factorial(n)    
# print(result)

#factorial using recursion 
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
   
# num= int(input("Enter number:"))
# print("Factorial=",factorial(num))   

#Function that reverses a list. 
# def reverse_list(num):
#     reversed_list=[]
#     for item in num:
#          reversed_list.insert(0, item)
#     return reversed_list

# my_list=[1,2,3,4,5]
# print(reverse_list(my_list))

#✅ Reverse List Using Slicing + Print Format
# def reverse_list(list):
#     return list[::-1]

# my_list=[1,2,3,4,5]
# print(reverse_list(my_list))

#Using built-in reverse()
# def reverse_list(list):
#     list.reverse()
#     return list

# my_list=[1,2,3,4,5]
# print(reverse_list(my_list))

# Function that finds max & min without using max(), min() 

# def  minmax(list):
#     maximum=list[0]
#     minimum=list[0]

#     for num in list:
#         if num>maximum:
#             maximum=num

#         if num< minimum:
#             minimum=num
            
#     return maximum, minimum

# my_list=[12,3,20,5,3,30,9]
# max_value, min_value= minmax(my_list)
# print("Maximum value:", max_value)
# print("Minumum value:", min_value)

# def sum_list(lst):
#     sum=0
#     for num in lst:
#         sum+=num
#     return sum
           
# my_list=[1,2,3,4,5]  
# print("Sum=",sum_list(my_list))      
        
#Function to check palindrome string.   

# def is_palindrome(s):
#     s = s.lower()              # case-insensitive check
#     if s == s[::-1]:           # reverse string compare
#         return True
#     else:
#         return False

# word = "Madam"
# print(is_palindrome(word))

# def is_palindrome(s):
#     s_lower = s.lower()
#     return s_lower == s_lower[::-1]

# word = "Madam"
# print("Reversed:", word[::-1])
# print("Is palindrome?", is_palindrome(word))

# using number 
# def reverse_number(num):
#     reversed_num=0
#     digit=0
#     while num > 0:
#         digit=num% 10          # last digit nikalna 
#         reversed_num=reversed_num * 10 + digit #  reverse me add karna 
#         num= num// 10 # last digit remove karna 
#     return reversed_num

# number=12345
# print("original number:",number)   
# print("Reversed number:", reverse_number(number))

# def total(*number):
#     sum=0
#     for num in number:
#         sum+=num
#     return sum 

# print(total(5,10,15))
# print(total(1,2,3,4,5,6))
    
def square(n):
    return n * n
def double_square(n):
    return square(n) * 2
print(double_square(5))    