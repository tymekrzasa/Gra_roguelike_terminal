class GameMap:
    def __init__(self, width:int, height:int):

        self.width = width
        self.height = height

    def is_inside(self, x:int, y:int) -> bool:

        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, player):
        for y in range(self.height):
            print("+———" * self.width + "+")
            row = "│"
            for x in range(self.width):
                if(x == player.x and y == player.y):
                    row += f" {player.char} │"
                else:
                    row += "   │"
            print(row)
        print("+———" * self.width + "+")
