class Character:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 1
        print(f"Moved left to ({self.x}, {self.y})")

    def move_right(self):
        self.x += 1
        print(f"Moved right to ({self.x}, {self.y})")

    def move_up(self):
        self.y -= 1
        print(f"Moved up to ({self.x}, {self.y})")

    def move_down(self):
        self.y += 1
        print(f"Moved down to ({self.x}, {self.y})")

# Creating a character at position (2, 3)
player = Character(2, 3)

# Moving the character
player.move_left()   # (1, 3)
player.move_right()  # (2, 3)
player.move_up()     # (2, 2)
player.move_down()   # (2, 3)
