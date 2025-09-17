# Types of Arguments

# 1.Default Arguments

# def average(a=1,b=3):
#     return (a+b)/2

# print(average(5))

# 2.Keyword arguments

# def average(a=1,b=3):
#     return (a+b)/2

# print(average(b=11,a=3))

# 3.Required arguments

# def average(a,b,c=1):
#     print((a+b+c)/2)

# average(a=3,b=3)
# average(8,7)
# Required = no default, must pass.
# Optional = has default, can skip.

# 4.Variable-length arguments

# i.Arbitrary Arguments:
def average(*nums):
    for i in nums:
        print(i)

def average(*nums):
    print(nums[0],nums[1],nums[2],nums[3])

average(2,3,5,9)

# ii.Keyword Arbitrary Arguments:

def name(**name):
    print(name["fname"],name["mname"],name["lname"])

name(fname="Fahad",lname="Patel",mname="Javedakhtar")

# Note: If list/tuple -- use *name(1 star)
#       If Dictionary -- use **name(2 star)
    




