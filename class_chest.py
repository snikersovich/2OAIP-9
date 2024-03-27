class Chest:
    def __init__(self, volume, fullness, privacy, access):
        self.__volume = volume
        self.__fullness = fullness
        self.__privacy = privacy
        self.__access = access

    def open(self):
        self.__access = True
        print('Сундук был открыт')

    def close(self):
        self.__access = False
        print('Сундук был закрыт')

    def unprivate(self):
        self.__privacy = True
        print('Сундук был открыт')

    def private(self):
        self.__privacy = False
        print('Доступ к содержимому запрещён')

    def fill(self, amount):
        self.__fullness += amount
        print(f'Сундук был заполнен на {self.__fullness}')

    def empty(self, amount):
        self.__fullness -= amount
        print(f'Сундук был опустошен на {self.__fullness}')


chest = Chest(10, 5, True, False)
