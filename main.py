import os

from game import Game


def main():
    for level in os.listdir(os.getcwd() + "\\maps\\maps\\"):
        if not Game().start("\\maps\\maps\\" + level):
            return None
    print('You win!')


if __name__ == '__main__':
    main()
