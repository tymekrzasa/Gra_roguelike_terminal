from entity import Player

def main():
    player = Player(x=0, y=5)
    print(f"Postać ({player.char}) powstała na pozycji: X={player.x}, Y={player.y}")
    player.move(1, 0)
    print(f"Po ruchu nowa pozycja: X={player.x}, Y={player.y}")


if __name__ == "__main__":
    main()