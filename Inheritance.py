# Inheritance = allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(Parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_live = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
          print("WOOF!")

class Cat(Animal):
     def speak(self):
          print("MEOW!")
    
class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")
    

dog = Dog("scooby")
cat = Cat("garfield")
mouse = Mouse("mickey")

cat.speak()
mouse.speak()
dog.speak()