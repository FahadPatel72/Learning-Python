# Lambda function

# Normal function
# def add(a,b):
#     return a+b


# Lambda function
add = lambda a,b:a+b
mul = lambda x:x*2
tri = lambda x,y,z:x+y+z

# print(add(2,5))
# print(mul(5))
# print(tri(2,3,4))

# lambda+normal

# Passing a lambda as an argument to a normal function
def apply(func, x):
    return func(x)

result = apply(lambda n: n * 2, 5)
print(result)  


# Passing a normal function as an argument to a lambda
def square(x):
    return x * x

double_square = lambda f, x: 2 * f(x)

print(double_square(square, 3))  

