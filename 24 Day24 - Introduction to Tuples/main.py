# tup = (1) # pyhton will confused type written int full explanation inn notes
# tup = (1,) # this will return class tuple

tup = (2,5,4,8,7,5,"Fahad",1.2)
print(type(tup),tup)

# Indexing in tuple
print(tup[0])
print(tup[1])
print(tup[2])

# Slicing in tuple
print(tup[:])
print(tup[-1:])
print(tup[0:])
print(tup[:-3])

if "Fahad" in tup:
    print("Yes fahad is present")
else:
    print("No")

if 5 in tup:
    print("Yesss")
else:
    print("no this no.is not present")

tup2 = tup[0:2]
print(tup2)

# Jump index in tuple
# Tuple[start : end : jumpIndex]
print(tup[0:8:2])
print(tup[0::2])