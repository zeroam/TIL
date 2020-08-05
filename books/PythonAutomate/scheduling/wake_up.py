"""wake_up.py
5초 뒤 깨어나는 스레드 실행
"""
import threading, time


def take_a_nap():
    time.sleep(5)
    print("Wake up!")


print("Start of program")
thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()
print("End of program")
