from functools import reduce
# map function

def cube(x):
    return x*x*x

# print(cube(2))

l = [1,2,4,6,4,3]

# newl =[]
# for item in l:
#     newl.append(cube(item))

# print(newl)

# using map the thing become very easy
# Map method

# newl = list(map(cube,l))
newl = list(map(lambda x:x*x*x,l))

print(newl)

# Filter method

def filter_function(a):
    return a>2

newnewl = list(filter(filter_function,l))
print(newnewl)

# Reduce method
# Note:before using this make sure you import reduce at the top of code

numbers = [1,2,3,4,5]

# Calculate sum of numbers using reduce functions
redc = reduce(lambda x,y:x+y,numbers)
print(redc)

# Note:In this we don't have to convert into list at last 

# Note:For all methods be carefull keep in mind all 3 are higher order functions means we can pass another function as an arguments into this function


