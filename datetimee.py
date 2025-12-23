# currect date 
# import datetime

# x= datetime.date.today()
# print(x)

# current datetime
# import datetime
# x= datetime.datetime.now()
# print(x)

#specific date 
# import datetime
# d = datetime.date(2025,1,20)
# print(d)

# date ke parts kaise nikalte hai 
# import datetime
# x = datetime.date.today()

# print(x.year)
# print(x.month)
# print(x.day)

# specific datetime banana 
# import datetime
# dt=datetime.datetime(2025 , 12, 10, 3, 42 , 40)
# print(dt)

#date format karna  (strftime())
# import datetime 
# x = datetime.datetime.now()

# print(x.strftime("%d-%m-%Y"))
# print(x.strftime("%A"))
# print(x.strftime("%B"))

# format       meaning 
# %d          Day(01-31)
# %m          Month(01-12)
# %Y          Year(2025)
# %A          Weekday name
# %B          Month name

# date difference ( days calculate karna )
# import datetime

# d1= datetime.date(2025,1,1)
# d2= datetime.date(2025,2,1)

# diff = d2-d1
# print(diff.days)

# #date Add / Substract karna 
# import datetime
# s=datetime.date.today()
# after_10_days =s+ datetime.timedelta(days=20)
# print(after_10_days)

#date.today() - aaj ki date 
#datetime.now() - current date + time
#strftime()- date ko format karta hai 
#timedelta()- date modify karna (add/ substract )