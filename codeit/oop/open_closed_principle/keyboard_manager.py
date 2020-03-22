from abc import ABC, abstractmethod


class Keyboard(ABC):

    @abstractmethod
    def save_input(self, input):
        pass

    @abstractmethod
    def send_input(self):
        pass


class SamsungKeyboard(Keyboard):

    def __init__(self):
        self.user_input = ""

    def save_input(self, input):
        self.user_input = input

    def send_input(self):
        return self.user_input
    

class AppleKeyboard(Keyboard):

    def __init__(self):
        self.keyboard_input = ""

    def save_input(self, input):
        self.keyboard_input = input

    def send_input(self):
        return self.keyboard_input


class KeyboardManager:

    def __init__(self):
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        self.keyboard = keyboard

    def get_keyboard_input(self):
        if isinstance(self.keyboard, Keyboard):
            return self.keyboard.send_input()
        return None


if __name__ == '__main__':
    keyboard_manager = KeyboardManager()

    apple_keyboard = AppleKeyboard()
    samsung_keyboard = SamsungKeyboard()

    keyboard_manager.connect_to_keyboard(apple_keyboard)
    apple_keyboard.save_input("안녕하세요")
    print(keyboard_manager.get_keyboard_input())

    keyboard_manager.connect_to_keyboard(samsung_keyboard)
    samsung_keyboard.save_input("안녕하세요")
    print(keyboard_manager.get_keyboard_input())
