# Recursion in Python

# Factorial of a number 

# factorial(0)=1
# factorial(1)=1
# factorial(2)=2*1
# factorial(3)=3*2*1
# factorial(3) = 3 * factorial(2)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Print fibonacci series

# fib(0)=0
# fib(1)=1
# fib(2)=fib(1)+fib(0)
# fib(n)=fib(n-1)+fib(n-2)

def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(11))