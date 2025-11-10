import random

yourName = input("Enter your name: ")
print("Welcome to KBC", yourName)

listQ = ["Who is the current prime minister of india?","Which current indian player break the record of sachin tendulkar in odis?","What is the full form of GDP?","Which team is the current ipl champion?"]

listA = ["Narendra Modi","Virat Kohli","Gross Domestic Product","RCB"]

score = 0

def kbcFun(ques,score):

    questions = random.choice(ques)
    print(questions)

    print("a.",listA[0])
    print("b.",listA[1])
    print("c.",listA[2])
    print("d.",listA[3])


    answerq = input("What is the option you are going: ")

    if answerq == "a":
        # print(listA.index(listA[0]))
        if listA.index(listA[0]) == ques.index(questions):
            print("You are correct")
            score = score + 10
            kbcFun(listQ,score)
        else:
            print("Answer is wrong")
            print("You can take the amount to your home is",score)
            
    elif answerq == "b":
        # print(listA.index(listA[1]))
        if listA.index(listA[1]) == ques.index(questions):
            print("You are correct")
            score = score + 10
            kbcFun(listQ,score)
        else:
            print("Answer is wrong")
            print("You can take the amount to your home is",score)

    elif answerq == "c":
        # print(listA.index(listA[2]))
        if listA.index(listA[2]) == ques.index(questions):
            print("You are correct")
            score = score + 10
            kbcFun(listQ,score)
        else:
            print("Answer is wrong")
            print("You can take the amount to your home is",score)
            
    elif answerq == "d":
        # print(listA.index(listA[3]))
        if listA.index(listA[3]) == ques.index(questions):
            print("You are correct")
            score = score + 10
            kbcFun(listQ,score)
        else:
            print("Answer is wrong")
            print("You can take the amount to your home is",score)
            
    else:
        print("Your input is incorrect")
        print(score)



kbcFun(listQ,score)