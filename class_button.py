class Button:
    def __init__(self, text, color_bg, color_text, size):
        self.text = text
        self.color_bg = color_bg
        self.color_text = color_text
        self.size = size
        self.active = True

    def click(self):
        print('Кнопка нажата')

    def change_color(self, new_color):
        self.color_bg = new_color
        print('Цвет изменен на: ')

    def change_text(self, new_text):
        self.text = new_text
        print('Текст обновлен')

    def change_size(self, new_size):
        self.size = new_size
        print('Размер текста изменен')

    def make_inactive(self):
        self.active = False
        pass

    def make_active(self):
        self.active = True
        pass


button = Button(1, 'red', 'push', 4,)