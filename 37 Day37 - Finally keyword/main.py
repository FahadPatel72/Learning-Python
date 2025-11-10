l=[1,5,3,2]

def func(l):
    try:
        i = int(input("Enter the index number:"))
        print(l[i])
        # return 1
    
    except:
        print("Some error occured")
        # return 0
    
    else:
        print("Code executed")
 
    finally:
        print("I will alway execute at the end")

func(l)

