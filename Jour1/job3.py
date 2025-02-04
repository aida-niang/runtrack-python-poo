class Operation:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        result = self.number1 + self.number2
        print("Result of addition:", result)

# Instantiate the class
operation1 = Operation(5, 10)

# Call the addition method
operation1.addition()
