class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_points(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def display_x(self):
        print(f"X coordinate: {self.x}")

    def display_y(self):
        print(f"Y coordinate: {self.y}")

    def change_x(self, new_x):
        self.x = new_x

    def change_y(self, new_y):
        self.y = new_y

# Creating an instance of the Point class
point1 = Point(5, 10)

# Displaying the coordinates
point1.display_points()

# Displaying individual coordinates
point1.display_x()
point1.display_y()

# Changing values of x and y
point1.change_x(15)
point1.change_y(20)

# Displaying the updated coordinates
point1.display_points()
