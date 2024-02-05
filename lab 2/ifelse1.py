#If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#elif example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
#else example

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#One line if statement:

if a > b: print("a is greater than b")


#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#a = 33
b = 200

if b > a:
  pass