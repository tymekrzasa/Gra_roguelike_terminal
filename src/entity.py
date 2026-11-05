import random
class Entity:
    def __init__(self, x:int, y:int, char:str):

        self.x = x
        self.y = y

        self.char = char

        self._hp = 100

    def move(self, dx:int, dy:int):

        self.x += dx
        self.y += dy

class Player(Entity):
    def __init__(self, x:int, y:int):
        super().__init__(x,y, char = "*")

class Enemy(Entity):
    def __init__(self, x:int, y:int, char:str):
            super().__init__(x, y, char)

    def random_movement(self, game_map):
        directions = [(1, 0),(0, 1),(0, 0),(-1, 0),(0, -1)]
        dx, dy = random.choice(directions)

        if(game_map.is_inside(self.x + dx, self.y +dy)):
             self.move(dx, dy)