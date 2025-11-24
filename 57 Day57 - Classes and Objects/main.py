# class
class Info:
    name="Fahad"
    age=23
    occupation="Software Developer"
    networth=10
    def call(self):   
        print(f"{self.name} is a {self.occupation}")

a = Info()
# print(a.name)
a.name = "Sameer"
a.age=36
a.call()
# print(a.name,a.age)

b = Info()
b.name = "Salman"
b.occupation = "African Manager"
b.call()

c = Info()
c.call()


# self
# the self is a reference to the current instance of the class, and is used to access variable belongs to the class like this in js.