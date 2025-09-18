l = [74,101,54,2,5,6,4]
print(l)

# l.append(43)  # Insert new item at the end of list
# print(l)

# l.sort() # Sort the list in ascending order
# print(l)

# l.sort(reverse=True) # Sort the list in descending order
# print(l)

# l.reverse() # Just Reverse the original string
# print(l)

m = [4,5,6,56,45,66,305,204]
print(m)
# m.insert(2,877) #insert 877 at index 2 in m list but it does not replce the previous index 2 item it just place this and existing will go on index 3 
# print(m)

# l.extend(m) #insert m string items at the end of l list
# print(l)

# j = m.copy() #copy elements from m list to new j list
# print(m)
# print(j)

j = l+m # Concatenate l and m list to new j list
print(j)

print(j.index(101)) # return first occurence index where this 101 item in list j

print(j.count(4))  #count how many times 4 is present in list j
