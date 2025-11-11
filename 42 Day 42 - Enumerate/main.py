marks = [23,43,44,42,97,3,4,12]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==4):
#         print("Awesome Fahad!")
#     index=index+1

# With the help of enumerate we don't have to declared index outside for loop and don't have to initialize everytime after a iteration

# for index,mark in enumerate(marks):
#     print(mark)
#     if(index==4):
#         print("Awesome Fahad!")


# Bydefault the enumerate start index from 0 if we want to start from 1 then see below  
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("Awesome Fahad!")
