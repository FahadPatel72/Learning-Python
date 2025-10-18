# f-Strings Old Method
name="fahad"
country="india"
str = "Hello I am from {1} and my name is {0}"
# print(str.format(country,name))
print(str.format(name,country))


# New f-Strings Method
print(f"Hello I am from {country} and my name is {name}")
price = 29.8722
print(f"I will get {price:.2F} dollars per week")


# convert into strings
print(f"{2 * 30}")



