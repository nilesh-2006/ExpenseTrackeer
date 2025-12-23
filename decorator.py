#Function Call Se Pehle & Baad Me Message

# def my_decorator(func):
#     def wrapper():
#         print("Function call se pehle kuch ho raha hai..")
#         func()
#         print("Function call ke baad kuch ho raha hai...")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello, Nilesh ! ")    

# greet()    

#Login Check 
# def login_required(func):
#     def wrapper():
#         print("Login check") 
#         func()   
#     return wrapper

# @login_required
# def dashboard():
#     print(" Welcome to Dashboard") 

# dashboard()  

#Logging (Track karna ki function kab call hua) 
# def log(func):
#     def wrapper():
#         print(f"{func.__name__} function call hua")  
#         func()
#     return wrapper

# @log
# def add():
#     print("Adding numbers....")    
# add()   

# Using the @changecase decorator on two functions: 
# def changecase(func):
#     def myinner():
#         return func().upper() 
#     return myinner

# @changecase
# def greet():
#     return "Hello Nilesh"   

# @changecase
# def myfun():
#     return "I am hacker"

# print(greet())
# print(myfun())

#Functions with arguments can also be decorated: 
def changecase(func):
    def wrapper(x):
        return func(x).upper()       
    return wrapper

@changecase
def myfun(name):
    return "hello " + name

print(myfun("Nilesh"))    