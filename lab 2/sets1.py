#set example
ourset = {100, "Dog", 3.14, 0, False , "a", "b", "c"}

print(ourset)

for section in ourset:
    print(section)
    print(section)
    
print(type(ourset))

#printing exact item
ourset = {100, "Dog", 3.14, 0, False , "a", "b", "c"}

print("Dog" in ourset)


# add() and remove() functions
ourset = {100, "Dog", 3.14, 0, False , "a", "b", "c"}

ourset.add("Cat")
ourset.add(2400)

ourset.remove(100)
ourset.remove(0)
print(ourset)

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)