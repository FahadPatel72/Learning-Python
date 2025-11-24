class Person:
    
    # def __init__(self):
    #     print("I am a default constructor")

    def __init__(self,name,occupation):
        print("I am a parameterized constructor")
        self.name = name
        self.occupation = occupation


    def info(self):
        print(f"{self.name} is a {self.occupation}")


# a = Person()
# print(a.name)

# Default Constructor - Everytimes call when you defined new class
# a = Person()

# Parameterized Constructor -- Compulsor pass the arguments 
a = Person("Fahad","Developer")
a.info()

# a = Person("Fahad","Developer",32) Error can't pass 4 arguments the constructor expects 2 .why 4 - one argument is self itself it automatically pass from here

# a= Person() -- error the constrcutor expects 2 arguments compulsory


