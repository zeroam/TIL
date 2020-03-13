from counter import Counter

class Clock:
    """
    시계 클래스
    """
    HOURS = 24 # 시 최댓값
    MINUTES = 60 # 분 최댓값
    SECONDS = 60 # 초 최댓값

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
        현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
        """
        self.hour = Counter(Clock.HOURS)
        self.hour.set(hour)
        self.minute = Counter(Clock.MINUTES)
        self.minute.set(minute)
        self.second = Counter(Clock.SECONDS)
        self.second.set(second)


    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)


    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킬 때, 분 또는 시가 바뀌어야하는 경우도 처리한다.
        """
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
        return f'{self.hour}:{self.minute}:{self.second}'
        

if __name__ == '__main__':
    # 초가 60이 넘을 때 분이 늘어나는지 확인하기
    print("시간을 1시 30분 48초로 설정합니다")
    clock = Clock(1, 30, 48)
    print(clock)

    # 13초를 늘린다
    print("13초가 흘렀습니다")
    for i in range(13):
        clock.tick()
    print(clock)

    # 분이 60이 넘을 때 시간이 늘어나는지 확인
    print("시간을 2시 59분 58초로 설정합니다")
    clock.set(2, 59, 58)
    print(clock)

    # 5초를 늘린다
    print("5초가 흘렀습니다")
    for i in range(5):
        clock.tick()
    print(clock)

    # 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
    print("시간을 23시 59분 57초로 설정합니다")
    clock.set(23, 59, 57)
    print(clock)

    # 5초를 늘린다
    print("5초가 흘렀습니다")
    for i in range(5):
        clock.tick()
    print(clock)