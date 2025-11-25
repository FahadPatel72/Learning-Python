# Decorators in python

def greet(fx):
    def mfx(*args,**kwargs):
        print("Welcome to learning")
        fx(*args,**kwargs)
        print("Thanks for watching my video")
    return mfx

# @greet
def hello():
    print("Hello World")

# hello()
# greet(hello)()

def add(a,b):
    print(a+b)

greet(add)(5,5)





