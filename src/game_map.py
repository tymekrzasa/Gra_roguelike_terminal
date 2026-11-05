class GameMap:
    def __init__(self, width:int, height:int):

        self.width = width
        self.height = height

    def is_inside(self, x:int, y:int) -> bool:

        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, entities:list):
        for y in range(self.height):
            print("+———" * self.width + "+")
            row = "│"
            for x in range(self.width):
                char_to_draw = " "
                for entity in entities:
                    if(x == entity.x and y == entity.y):
                        char_to_draw = entity.char
                        break
                row += f" {char_to_draw} │"
            print(row)
        print("+———" * self.width + "+")
