mylist = ["apple", "banana", "cherry"]

print(mylist)

#list items are indexed, the first item has index [0], the second item has index [1] etc.

print(mylist[0])

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(type(list1))
print(type(list2))
print(type(list3))

#list can contain different data types 
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# By using append() or inser() function we can add items to our list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove() function removes specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist1.pop()
print(thislist1)

# Loop through list by using for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  
# You can loop through the list items by using a while loop.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)