
list1 = ["red", "blue", 'green']
list2 = list()  # empty
list3 = []  # empty

cities = ["St. Petersburg", "Clearwater",
          "Jacksonville", "Palo Alto", "Pittsburgh"]

print(cities)
print(len(cities))
print(cities[0], cities[3])

cities.append("Paris")
cities.append("Tarpon Springs")

print(cities)

cities.insert(0, "Harrisburg")
cities.insert(2, "Philadelphia")
print(cities)

more_cities = ['Dunedin', 'San Jose', 'Durham']

cities.extend(more_cities)
print(cities)

# junk = ['a', 'b', 'c']
# cities.append(junk)
# print(cities)

# LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[2]  # del LIST[pos]  del OBJ
print(cities)

city = cities.pop()
print(city)
print(cities)

city = cities.pop(0)
print(city)
print(cities)

cities.remove("Paris")
print(cities)

# del LIST[pos]    x = LIST.pop(pos)  LIST.remove(value)

city = "Palo Alto"
pos = cities.index(city)
print(f"{city} is at position {pos}")

foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', ]
print(foods.count('eggs'), foods.count('spam'))

print(cities)

print(cities[0], cities[4], cities[7])

print(cities[len(cities) - 1])
print(cities[-1])
print(cities[-2])

print(cities[0:3])  #  elements 0, 1, 2    0 + 3 items
print(cities[3:5])  #  elements 3,4        3 + 2 items

# slice   LIST[START:STOP]  LIST[:STOP] LIST[START:]
#          LIST[START:STOP:STEP]

print()

# for VAR in ITERABLE:
for city in cities:   # 'foreach'
    #  city = <NEXT-ELEMENT-OF> cities
    print(city)


print()

x = "abcde"
for char in x:
    print(char)
print()


print(cities)
print(len(cities), min(cities), max(cities))
print(sorted(cities), '\n')

for i, value in enumerate(cities):
    print(i, value)
print()

for city in reversed(cities):
    print(city)
print()

e = enumerate(cities)
print(e)

r = reversed(cities)
print(r, '\n')

print("round 1:")
for i, city in e:
    print(i, city)
print()

print("round 2:")
for i, city in e:
    print(i, city)
print()

