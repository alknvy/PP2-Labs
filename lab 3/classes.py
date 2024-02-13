#Task 1
class StringManipulator():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.string.upper())

s=StringManipulator()
s.getString()
s.printString()

#Task 2
class Shape():
    def __init__(self):
        pass

    def area():
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    
    def area(self):
        return self.length*self.length
n=int(input("give length:"))
square=Square(n)
print(square.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width
    
    def area(self):
        return self.length * self.width
n=int(input("give length:"))
m=int(input("give width:"))
rectangle=Rectangle(n,m)
print(rectangle.area())

#task 3
import math
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y        

    def show(self):
        return self.x, self.y
    
    def move(self, newx, newy):
        self.x=newx
        self.y=newy
    
    def dist(point1, point2):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

n=Point(1,2)
print(n.show())
point1 = Point(3, 4)
point2 = Point(6, 8)
print("Distance between point1 and point2:", Point.dist(point1, point2))

#task 4
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


#task 5
# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)
