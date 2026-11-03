from entity import Player
from game_map import GameMap
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    player = Player(x=5, y=5)
    game_map = GameMap(width=10, height=10)

    while True:
        clear_screen()
        print("Witaj w grze typu Roguelike")
        print("sterowanie w/a/s/d góra/lewo/dół/prawo \nq wychodzenie z gry")
        game_map.render(player=player)
        

        move = input("\nTwój ruch: ").strip().lower()

        if(move == 'q'):
            print("wychodzenie z gry")
            break
        elif move == 'w':
            if (game_map.is_inside(player.x, player.y - 1)):
                player.move(0, -1)
        elif move == 'a':
            if (game_map.is_inside(player.x - 1, player.y)):
                player.move(-1, 0)
        elif move == 's':
            if (game_map.is_inside(player.x, player.y + 1)):
                player.move(0, 1)
        elif move == 'd':
            if (game_map.is_inside(player.x + 1, player.y)):
                player.move(1, 0)

if __name__ == "__main__":
    main()