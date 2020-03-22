from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def short_message(self):
        pass


class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_nofitications = []

    def add_new_message(self, new_message: Message):
        """새로 온 메시지 추가"""
        self.message_nofitications.append(new_message)
        
    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_nofitications:
            print(message.short_message() + '\n')


class KakaoTalkMessage(Message):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def short_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = '{}\n{}\n'.format(self.time, self.sent_by)
        if len(self.content) <= KakaoTalkMessage.notification_message_max_len:
            message_str += self.content
        else:
            message_str += self.content[:KakaoTalkMessage.notification_message_max_len]
            message_str += '...'

        return message_str


class FacebookMessage(Message):
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def short_message(self):
        """메시지를 짧은 형태로 리턴함"""
        res_str = '{}\n{}\n{}\n'.format(self.time, self.sent_by, self.location)
        if len(self.content) <= FacebookMessage.notification_message_max_len:
            res_str += self.content
        else:
            res_str += self.content[:FacebookMessage.notification_message_max_len]
            res_str += '...'

        return res_str


class TextMessage(Message):
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def short_message(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = '{}, {}\n'.format(self.sent_by, self.time)
        if len(self.content) <= TextMessage.notification_message_max_len:
            noti_string += self.content
        else:
            noti_string += self.content[:TextMessage.notification_message_max_len]
            noti_string += '...'

        return noti_string


if __name__ == '__main__':
    # 메시지 알림 관리 인스턴스 생성
    message_notification_manager = MessageNotificationManager()

    # 서로 다른 종류의 메시지 3개 생성
    kakao_talk_message = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같아, 미안!")
    facebook_message = FacebookMessage("고대위", "서울시 성북구", "2019년 7월 1일 오후 11시 35분", "아니다, 갈게! 너네 어디서 놀고 있어?")
    text_message = TextMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게, 나 지금 출발")

    # 메시지 알림 관리 인스턴스에 3개의 메시지를 추가
    message_notification_manager.add_new_message(kakao_talk_message)
    message_notification_manager.add_new_message(facebook_message)
    message_notification_manager.add_new_message(text_message)

    # 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
    message_notification_manager.display_message_notifications()            
