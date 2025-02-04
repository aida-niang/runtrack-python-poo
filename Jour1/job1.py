class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
operation1 = Operation()

# Affichage de l'objet
print(operation1)  # Cela affichera l'adresse mémoire de l'objet

# Pour afficher les valeurs des attributs :
print(f"Nombre1: {operation1.nombre1}, Nombre2: {operation1.nombre2}")
