# Mutating in python
tuple2 = (2,4,6,7,32,2)
lst = list(tuple2)
lst[3] = 77
lst[0] = 34
tuple2 = tuple(lst)
print(tuple2)

tuple3 = (5,3,4,5,5,32,2)

# tuplenew = tuple2+tuple3
# print(tuplenew)

# Concatenate two tuples
lst2 = list(tuple2)
lst3 = list(tuple3)
lst3.extend(lst2)
tuple3 = tuple(lst3)
print(tuple3)

# Count Method in tuple
print(tuple3.count(5))

# index - return first occurence of the element it returns its index
# print(tuple3.index(5,0,2))
                      # 5 0:2 = [2,3,4,5] == 3
print(tuple3.index(5,0,2))
