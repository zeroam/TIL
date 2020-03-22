from abc import ABC, abstractmethod


class IMessage(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass


class Email(IMessage):
    def __init__(self, content, owner_email):
        """이메일은 그 내용과 보낸 사람의 이메일 주소를 인스턴스 변수로 가짐"""
        self._content = content
        self.owner_email = owner_email

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """이메일 내용 수정 메소드"""
        self._content = self.owner_email + "님의 메일\n" + new_content

    def send(self, destination):
        """이메일 전송 메소드"""
        print("{}에서 {}로 이메일 전송!\n내용: {}").format(self.owner_email, destination, self._content)
        return True


class TextMessage(IMessage):
    def __init__(self, content):
        """문자 메시지는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """문자 메시지 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """문자 메시지 전송 메소드"""
        print("{}로 문자 메시지 전송!\n내용: {}").format(destination, self._content)


class Memo(IMessage):
    """포스트잇 메시지 클래스"""
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content

    def edit_content(self, new_content):
        self._content = new_content

    def send(self, destination):
        # 인터페이스가 사용하지도 않을 메서드를 강제하고 있는 상황
        print('메모는 아무 데도 보낼 수 없습니다!')
        return False


class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IMessage):
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)


if __name__ == '__main__':
    email = Email('이메일 메시지', 'young@codeit.kr')
    text_message = TextMessage('텍스트 메시지')
    memo = Memo('메모 메시지')

    text_reader = TextReader()

    text_reader.add_text(email)
    text_reader.add_text(text_message)
    text_reader.add_text(memo)

    text_reader.read_all_texts()
