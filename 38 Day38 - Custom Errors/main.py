# i = int(input("Enter the number between 5 and 9:"))

# if(i<5 or i>9):
#     raise ValueError


i = int(input("Enter the number between 5 and 9:"))

if i.lower() == "quit":
    print("Exciting program")

elif(i<5 or i>9):
    raise ValueError


    


    