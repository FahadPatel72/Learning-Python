# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# for encoding
userInput = input("Enter your name:")

lst = list(userInput)

fcode = ["w","e","f"]
bcode = ["s","v","j"]

if(len(lst)>3):
   fele = lst.pop(0)
   lst.append(fele)

   for item in fcode:
      lst.insert(0,item)
   
   for ele in bcode:
      lst.append(ele)

else:
   lst.reverse()

print(lst)
print("Great now you have encoded the string")
# separator = ", "
# userInput = separator.join(lst)
# print(userInput)

# for decoding

userIn = input("Are you want to decode the string or want to exit,type yes for decode and exit for exit:")

# Decode the string 

if(userIn == "yes"):

   if(len(lst)>3):
      del lst[0:3]
      del lst[-3:]
      
      litem = lst.pop(len(lst)-1)
      
      lst.insert(0,litem)

   else:
       lst.reverse()

elif(userIn=="exit"):

   separator = ", "
   userInput = separator.join(lst)
   print(userInput)


else:
   separator = ", "
   userInput = separator.join(lst)
   print(userInput)


separator = ", "
userInput = separator.join(lst)
print(userInput)