l = [5,3,4,5]
print(l)

marks = [3,5,7,9,"Fahad",3.2]
print(marks)

# marks[1]=8
# print(marks)

# # Note:  a single list can contain items of different data types.

# # List Index
# print(marks[3])

# # Positive Indexing
# print(marks[2])
# print(marks[:])
# print(marks[0:])
# print(marks[:5])

# # Negative Indexing
# print(marks[-2])
# print(marks[-1:])
# print(marks[:-2])

# # Check whether an item in present in the list?
# if "Fahad" in marks:
#     print("Yes you are absolutely correctly")
# else:
#     print("No Better Luck , Next Time!")

# if "had" in marks:
#     print("Yes bro")
# else:
#     print("No Sorry Bro")


# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if 10 in marks:
#     print("Yes marks is there")
# else:
#     print("No marks is not present")

# Jump Index
# marks[startIndex,endIndex,jumpIndex]
print(marks[0:5:2])
print(marks[0:6:3])

# List Comprehension
lst = [i for i in range(0,4)]
print(lst)

lst = [i*i for i in range(0,4)]
print(lst)

lst = [i for i in range(0,11) if (i%2==0)]
print(lst)

lst = [i for i in range(0,11) if (i%2==1)]
print(lst)