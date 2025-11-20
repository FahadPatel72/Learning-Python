# Global and local variables

x=3 # Global Variable

def hello():
    y = 9 # Local Variable
    x=5
    # print(y)
    # print(x)

# hello()
print(x)

# if we want to change global variable from function we can change by using global

def my_function():
    global x # Access global scope of x and and mutate 
    x=10
    y=2
    print(y)

my_function()
print(x)

