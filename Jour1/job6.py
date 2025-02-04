class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""

    def grow_older(self):
        self.age += 1

    def set_name(self, name):
        self.name = name

# Creating an instance of Animal
animal1 = Animal()

# Displaying the initial age
print("Animal's age:", animal1.age)

# Making the animal grow older
animal1.grow_older()
print("Animal's age after growing older:", animal1.age)

# Naming the animal
animal1.set_name("Buddy")
print("Animal's name:", animal1.name)
