#First example

x = 5
y = "John"
print(x)
print(y)


#Second example

a = 4
A = "Sally"
#A will not overwrite a

#Third example

myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Fourth example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Fifth example

n = b = m = "Orange"
print(n)
print(b)
print(m)

#Sixth example
fruits = ["apple", "banana", "cherry"]
X, Y, Z = fruits
print(X)
print(Y)
print(Z)

#Seventh example
Q = "Python"
W = "is"
E = "awesome"
print(Q, W, E)

#Eighth example
J = 5
L = "John"
print(J , L)

#Ninth example
u = "awesome"

def myfunc():
  global u
  u = "fantastic"

myfunc()

print("Python is " + u)