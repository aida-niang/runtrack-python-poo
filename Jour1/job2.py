class Operation:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

# Instantiate the class
operation1 = Operation()

# Print attribute values
print("Value of number1:", operation1.number1)
print("Value of number2:", operation1.number2)

operation2 = Operation(5, 10)
print("Value of number1:", operation2.number1)
print("Value of number2:", operation2.number2)
