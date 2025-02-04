class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instantiate the class
operation1 = Operation()

# Object display
print(operation1)  # This will display the object's memory address

# To display attribute values :
print(f"Nombre1: {operation1.nombre1}, Nombre2: {operation1.nombre2}")
