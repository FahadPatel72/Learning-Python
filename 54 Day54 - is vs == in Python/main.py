# 'is' vs '==' in Python

# "is" compares exact location of objects in memory / compares identity
# "==" compares the values

a = 4
b = "4"

# print(a is b) #false
# print(a == b) #false

# a = "harry"
# b = "harry"

# a = [1,2,3]
# b = [1,2,3]

# a = (2,3)
# b = (2,3)

# a = None
# b = None

a=3
b=3

# print(a is None)
print(a is b)
print(a == b)