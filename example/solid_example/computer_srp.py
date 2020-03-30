class Computer:
    def __init__(self, mouse, keyboard, monitor):
        self.mouse = Mouse(mouse)
        self.keyboard = Keyboard(keyboard)
        self.monitor = Monitor(monitor, self.keyboard)


class Mouse:
    def __init__(self, name):
        self.name = name

    def click(self):
        print(f'{self.name}: 클릭')

    def right_click(self):
        print(f'{self.name}: 우클릭')


class Keyboard:
    def __init__(self, name):
        self.name = name
        self.data = ''

    def input(self, data):
        print(f'{self.name} 입력:')
        print(data)
        self.data += data

    def clear(self):
        self.data = ''


class Monitor:
    def __init__(self, name, keyboard):
        self.name = name
        self.keyboard = keyboard

    def display(self):
        print(f'{self.name} 출력:')
        print(self.keyboard.data)
        self.keyboard.clear()


if __name__ == '__main__':
    computer = Computer('samsung 마우스', 'logitech 키보드', 'LG 모니터')
    computer.mouse.click()
    computer.mouse.right_click()
    computer.keyboard.input('hello\n')
    computer.keyboard.input('nice to meet you\n')
    computer.monitor.display()
