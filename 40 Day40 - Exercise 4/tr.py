import random
import string 

def random_chars():
   return ''.join( random.choice(string.ascii_lowercase) for _ in range(3) )

# encoding

def encoding(word):

    if(len(word)>=3):
        core = word[0]
        str = word[1:] + core

        prefix = random_chars()
        suffix = random_chars()

        return prefix+str+suffix
    
    else:
        return word[::-1]


# decoding

def decoding(word):
    if(len(word)>=3):

        dstr = word[3:-3]
        core = dstr[-1]

        rstr = core + dstr[:-1]

        return rstr

    else:
        return word[::-1]


choice = input("Type 'code' to encode or 'decode' to decode: ")

text = input("Enter your string:")

if choice == "encode":
    result = encoding(text)
    print("Encoded:",result)

elif choice == "decode":
    result = decoding(text)
    print(result)

else:
    print("Invalid input")





