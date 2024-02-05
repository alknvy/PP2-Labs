ourdict = {
    "Make": "Porche",
    "Model": "991 Turbo S",
    "Color": "Black",
    "Year": 2024,
}

print(ourdict["Make"])
print(ourdict["Model"])
print(ourdict["Color"])
print(ourdict["Year"])

for item in ourdict.items():
    print(item)

print("===")
    
for values in ourdict.values():
    print(values)
    
print("===")

for key in ourdict.keys():
    print(key)
    




myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)