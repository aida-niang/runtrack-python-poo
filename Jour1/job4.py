class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def introduce_yourself(self):
        return f"My name is {self.first_name} {self.last_name}."

# Creating instances of the Person class
person1 = Person("Smith", "John")
person2 = Person("Doe", "Jane")

# Calling the introduce_yourself method
print(person1.introduce_yourself())
print(person2.introduce_yourself())
