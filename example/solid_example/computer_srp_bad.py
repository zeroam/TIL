class Computer:
    def __init__(self, mouse, keyboard, monitor):
        self.mouse = mouse
        self.keyboard = keyboard
        self.monitor = monitor
        self.input = ''

    def mouse_click(self):
        print(f'{self.mouse}: 클릭')

    def mouse_right_click(self):
        print(f'{self.mouse}: 우클릭') 

    def keyboard_input(self, data):
        self.input = self.input + data
        print(f'{self.keyboard} 입력:\n{data}')

    def monitor_display(self):
        print(f'{self.monitor} 출력:\n{self.input}')
        self.input = ''


if __name__ == '__main__':
    computer = Computer('samsung 마우스', 'logitech 키보드', 'LG 모니터')
    computer.mouse_click()
    computer.mouse_right_click()
    computer.keyboard_input('hello\n')
    computer.keyboard_input('nice to meet you\n')
    computer.monitor_display()
