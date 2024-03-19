'''class person:
    name = "Mohit"
    occupation = "student"
    networth = "10 trillion"
    def info(self):
        print(self.name, "is a ", self.occupation)

a = person()
b = person()
c = person()

a.name = "ram"
b.name = "shyam"
c.name = "john"
c.occupation = "engineer"

a.info()
b.info()
c.info()'''

'''
class dog:
    species = "human"
    def __init__(self, name, occupation) -> None:
        self.name = name 
        self.occupation = occupation
        pass
miles = dog("ram", "engineer")'''


'''
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Dog("Tom", 3)
print(miles.description())
print(miles.speak("bhau bhau"))
print(miles)'''


'''
class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"
    pass
print(Child.hair_color)
print(Parent.hair_color)'''

'''
# inheritance.py
class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")
        
print(Child.speaks)'''


'''
class Student:
    def __init__(self, name, city, state) -> None:
        self.name = name
        self.city = city
        self.state = state
    
    def information(self, kaksha):
        print(self.name,"is a student who lives in", self.city,",",self.state,"and studies in",kaksha)
    
data = Student("Mohit", "Indore", "MP")
data.information("2nd")
    '''