# Dictionary 
info = {
    "name":"Fahad",
    "education":"qualification",
    "age":23,
    231:"Hello Guys"
}

print(info)
print(info["name"])
print(info[231])

# This method also we can use
print(info.get("age"))

# Access that value which is not present in dictionary 
# print(info["name2"]) This will give error
print(info.get("name2")) # Return none instead of error use this to prevent errors

for item in info:
    print(info[item])

# For accessing keys
print(info.keys())

# For accessing values
print(info.values())

# We can print all the key-value pairs in the dictionary using items() method.
print(info.items())
for key,value in info.items():
    print(f"The {key} and {value} is very important for us")