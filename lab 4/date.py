import datetime

#task 1
def fivedays():
    today = datetime.date.today()
    tdelta = datetime.timedelta(days=5)
    print(today-tdelta)
    
print(fivedays())


print("===")

#task 2
def yesterday_today_tommorow():
    tdelta = datetime.timedelta(days=1)
    today = datetime.date.today()
    print(today-tdelta)
    print(today)
    print(today+tdelta)

print(yesterday_today_tommorow())

print("===")
#task 4
def difference_in_seconds():
    today = datetime.date.today()
    date = datetime.date(2024,1,12)
    dif = today - date
    print(dif.total_seconds())
    
print(difference_in_seconds())

print("===")
#task 3
def microseconds():
    dt = datetime.datetime.today().replace(microsecond=0)
    print(dt)
    
print(microseconds())