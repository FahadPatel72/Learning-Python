# Opening a file

# f = open('myfile.txt') Bydefault read 
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# Note: Everytime don't forget to close the file f.close()

# with write we can create new file and add text content or override existing file if exist
# f = open('myfile2.txt','w')
# f.write("Kaise ho sab")
# f.close()

# Append - Add content in existing file
# f = open('myfile.txt','a')
# f.write('Milte hai fir kabhi')
# f.close()

# Create a new file and if file already exist then gives error
# f = open('myfile2.txt','x')

# f = open('myfile2.txt','rb')
# text = f.read()
# print(text)
# f.close()

# with - the benefit of using with is we don't have to write f.close() everytime after every method we write.

# with open('myfile.txt','a') as f:
#     f.write("kem cho majama")





