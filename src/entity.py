import random
class Entity:
    def __init__(self, x:int, y:int, char:str, attack_power:int = 20):

        self.x = x
        self.y = y
        self.char = char
        self._hp = 100
        self.attack_power = attack_power

    def move(self, dx:int, dy:int):

        self.x += dx
        self.y += dy

    def is_alive(self) -> bool:
        return self._hp > 0
              
    def take_damage(self, damage:int):
         self._hp -= damage
         if self._hp < 0:
              self._hp = 0

    def attack(self, target:'Entity'):
        target.take_damage(self.attack_power)

class Player(Entity):
    def __init__(self, x:int, y:int):
        super().__init__(x,y, char = "*", attack_power = 25)

class Enemy(Entity):
    def __init__(self, x:int, y:int, char:str = "E"):
            super().__init__(x, y, char)

    def random_movement(self, game_map, player:'Entity'):
        directions = [(1, 0),(0, 1),(0, 0),(-1, 0),(0, -1)]
        dx, dy = random.choice(directions)

        target_x = self.x + dx
        target_y = self.y + dy

        if target_x == player.x and target_y == player.y:
            self.attack(player)
            print(f"--> Przeciwnik {self.char} zaatakował Cię za {self.attack_power} HP!")
        elif(game_map.is_inside(target_x, target_y)):
             self.move(dx, dy)