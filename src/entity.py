class Player:
    def __init__(self, x:int, y:int):

        self.x = x
        self.y = y

        self.char = "*"

        self._hp = 100

    def move(self, dx:int, dy:int):

        self.x += dx
        self.y += dy