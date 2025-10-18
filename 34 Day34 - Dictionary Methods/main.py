# Dictionary Methods

# update()

ep1 = {232:43,423:21,342:87,233:87}
print(ep1)
ep2 = {231:32,221:87}
print(ep2)

ep1.update(ep2)
print(ep1)

# Clear whole dictionary
# ep1.clear() # Output:{}
# print(ep1)

# Pop/remove one specific record from dictionary using its key name
ep1.pop(423)
print(ep1)

# Pop/remove last record from dictionary
ep1.popitem()
print(ep1)

# Delete dictionary specific item using del
# del ep2["221"] Can't used string instead originally it is number key returns error
del ep2[221]

print(ep2)