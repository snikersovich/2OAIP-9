from classes.class_button import Button


def main():
    button = Button(1, 2, 3, 4)
    button.click()
    button.change_color('red')
    button.change_text('push')
    button.change_size(4)
    button.make_inactive()
    button.make_inactive()


if __name__ == '__main__':
    main()