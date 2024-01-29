# Example 1
print("Hello")
print('Hello')

# Example 2 Multiline strings
a = """kfkfkfkfkfkjdjdjdj cdj cjdncjdncjdncjdnc
fvfvfvfnvfjvjufvifjvfiv
nfvfjvfjvnjfvnjdciew ceicdwjcerirjeirjcidjciedj"""
print(a)

# Example 3 Strings are array
a = "Hello, World!"
print(a[4])

# Example 4 loop trhough string 
for x in "banana":
  print(x)
  
#Example 5 we can check string
txt = "The best things in life are free!"
print("free" in txt)

# Or print if only "free" exists 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
# Check if "expensive" is NOT present in the following text
txt = "The best things in life are free!"
print("expensive" not in txt)

# We can slice a string 
b = "Hello, World!"
print(b[1:6])

# Slice from the start
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[2:])

# And negative indexing
b = "Hello, World!"
print(b[-5:-2])

# Returns string to upper case
a = "Hello, World!"
print(a.upper())

# Returns to lower case
a = "HELLO, WORLD!"
print(a.lower())

# Remove any whitespace strip()
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Concatenation 
a = "Hello"
b = "World"
c = a + b
print(c)

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))