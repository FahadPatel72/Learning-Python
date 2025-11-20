# readline method

f = open('myfile.txt','r')

line = f.readline()    

i=0
while True:
    i=i+1
    line = f.readline()
    m1 = int(line.split(",",[0]))    
    m2 = int(line.split(",",[1]))
    m3 = int(line.split(",",[2]))   

    print(m1)
    print(m2)
    print(m3) 
    


    