# seek() method

# with open('file.txt','r') as f:
#     print(type(f))

#     f.seek(10) # It skip first 10 characters and then start reading
#     data = f.read()
#     print(data)


# tell() method

# with open('file.txt','r') as f:
#     print(type(f))

#     f.seek(10) # It skip first 10 characters and then start reading
#     current_position = f.tell() # It checks upto which characters the reading has skip/stop
#     print(current_position)
#     data = f.read()
#     print(data)

# truncate method
with open('file2.txt','w') as f:
    f.write("Hello World") # Suppose we write Hello World in file2.txt

    f.truncate(5) # it truncate the Hello World in file2.txt to only Hello
    

