class Dog:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stimina = 100
    
    def bark(self):
        print(f"Woof!")
    
    def sayname(self):
        print(f"My name is {self.name}")

testDog = Dog("댕댕2")
testDog.bark()