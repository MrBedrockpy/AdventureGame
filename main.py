import os

from game import Game


def setup():
    os.system("pip install pygame cv2")


def main():
    setup()
    for level in os.listdir(os.getcwd() + "\\maps\\maps\\"):
        Game().start("\\maps\\maps\\" + level)


if __name__ == '__main__':
    main()
