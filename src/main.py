from entity import Player, Enemy
from game_map import GameMap
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    player = Player(x=5, y=5)
    goblin = Enemy(x=2,y=2,char="G")
    game_map = GameMap(width=8, height=8)
    entities = [player, goblin]

    while True:
        clear_screen()
        print("Witaj w grze typu Roguelike")
        print("sterowanie w/a/s/d góra/lewo/dół/prawo \nq wychodzenie z gry")
        game_map.render(entities)

        if not player.is_alive():
            print("Game over")


        move = input("\nTwój ruch: ").strip().lower()

        if(move == 'q'):
            print("wychodzenie z gry")
            break
        elif move == 'w':
            if (game_map.is_inside(player.x, player.y - 1)):
                player.move(0, -1)
                goblin.random_movement(game_map, player)
        elif move == 'a':
            if (game_map.is_inside(player.x - 1, player.y)):
                player.move(-1, 0)
                goblin.random_movement(game_map, player)
        elif move == 's':
            if (game_map.is_inside(player.x, player.y + 1)):
                player.move(0, 1)
                goblin.random_movement(game_map, player)
        elif move == 'd':
            if (game_map.is_inside(player.x + 1, player.y)):
                player.move(1, 0)
                goblin.random_movement(game_map, player)

if __name__ == "__main__":
    main()