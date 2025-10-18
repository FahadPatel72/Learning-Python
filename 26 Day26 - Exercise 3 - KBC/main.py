import random

yourName = input("Enter your name: ")
print("Welcome to KBC", yourName)

listQ = ["Who is the curren prime minister of india?","Which current indian player break the record of sachin tendulkar in odis?","What is the full form of GDP?","Which team is the current ipl champion?"]

listA = ["Narendra Modi","Virat Kohli","Gross Domestic Product","RCB"]

questions = random.choice(listQ)
print(questions)
print(listQ.index(questions))

print("a.",listA[0])
print("b.",listA[1])
print("c.",listA[2])
print("d.",listA[3])


answerq = input("What is the option you are going: ")

if answerq == "a":
    print(listA.index(listA[0]))
    if listA.index(listA[0]) == listQ.index(questions):
        print("You are correct")
    else:
        print("Answer is wrong")
elif answerq == "b":
    print(listA.index(listA[1]))
    if listA.index(listA[1]) == listQ.index(questions):
        print("You are correct")
    else:
        print("Answer is wrong")
elif answerq == "c":
    print(listA.index(listA[2]))
    if listA.index(listA[2]) == listQ.index(questions):
        print("You are correct")
    else:
        print("Answer is wrong")
elif answerq == "d":
    print(listA.index(listA[3]))
    if listA.index(listA[3]) == listQ.index(questions):
        print("You are correct")
    else:
        print("Answer is wrong")
else:
    print("Your input is incorrect")
