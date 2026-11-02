from entity import Player
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    player = Player(x=5, y=5)

    while True:
        clear_screen()
        print("Witaj w grze typu Roguelike")
        print(f"Postać znajduje się na pozycji X={player.x}, Y={player.y}")
        print("sterowanie w/a/s/d góra/lewo/dół/prawo \nq wychodzenie z gry")

        move = input("\nTwój ruch: ").strip().lower()

        if(move == 'q'):
            print("wychodzenie z gry")
            break
        elif move == 'w':
            player.move(0, 1)
        elif move == 'a':
            player.move(-1, 0)
        elif move == 's':
            player.move(0, -1)
        elif move == 'd':
            player.move(1, 0)

if __name__ == "__main__":
    main()