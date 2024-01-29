# Task 1 Use the len function to print the length of the string.
x = "Hello World"
print(len(x))
# Task 2 Get the first character of the string txt.
a = "Hello World"
x = a[0]
print(x)
# Task 3 Get the characters from index 2 to index 4 (llo).
a = "Hello World"
x = a[2 : 5]
print(x)
# Task 4 Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)
# Task 5 Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
print(txt)
# Task 6 Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
print(txt)
# Task 7 Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J" )
print(txt)
# Task 8 Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))