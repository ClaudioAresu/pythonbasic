class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("IDK")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak (self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and {self.color}")

class Dog(Pet):
   
    def speak (self):
        print("Au")

p = Pet("Tim", 19)
p.speak()
c = Cat("Bil", 2, "Brown")
c.show()