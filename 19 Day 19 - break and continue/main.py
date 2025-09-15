# for i in range(5):
#     print(i)

for i in range(12):
    if(i==10):
        print("Terminate from loop")
        break
    print("5 X",i+1 ,"=", 5*(i+1))


for i in range(12):
    if(i==10):
        print("Continue but just skip this iteration")
        continue
    print("5 X",i+1 ,"=", 5*(i+1))