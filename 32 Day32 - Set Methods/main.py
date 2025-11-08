# union Method

a = {1,2,4,5,6}
b = {3,6,8}
# print(a.union(b))

# union update method
# print(a,b)
# a.update(b)
# print(a)

# intersection method
# print(a.intersection(b))

# intersection update method
# a.intersection_update(b)
# print(a)

# symmetric_difference
# print(a.symmetric_difference(b))

# symmetric_difference_update
# a.symmetric_difference_update(b)
# print(a)

# difference
# print(b)
# print(b.difference(a))
# print(b)

# difference_update
# b.difference_update(a)
# print(b)

# isdisjoint():


cities = {"Tokyo", "Madrid", "Berlin", "Delhi","Seoul","Kabul"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.isdisjoint(cities2))

# issuperset():
print(cities.issuperset(cities2))

# issubset
print(cities2.issubset(cities))


# add method 
cities.add("London")
# print(cities)


# update method
cities3 = {"California","Bangalore","Abudhabi"}
cities.update(cities3)
# print(cities)

# remove()/discard()
# cities.remove("London2") # Gives error the city not present
# cities.discard("London2") # Not give error if the city not present

# pop -- remmove the last item of the set but we don't know which items got remove because the set is unordered

cities.pop()
# print(cities)

# del method -- remove the whole set
# print(cities3)
# del cities3
# print(cities3)

# clear method - just if we want to remove/clear the elements in set not delete whole set
# cities.clear()
# print(cities)

# Check if item exists
if "Bangalore" in cities:
    print("Yes the city exist")
else:
    print("The city not exist")