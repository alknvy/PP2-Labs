# it will print true or false 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))

#You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
myFunction()

# isinstance() function can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))