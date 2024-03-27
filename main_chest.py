from classes import class_chest
from classes.class_chest import Chest


def main():
    chest = Chest(10, 5, True, False)
    chest.open()
    chest.fill(3)
    chest.private()
    chest.close()


if __name__ == '__main__':
    main()