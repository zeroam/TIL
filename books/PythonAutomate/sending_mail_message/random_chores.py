"""random_chores.py
사람들의 이메일 주소 목록과 해야 할 잡일 목록을 받고,
무작위로 할당해 메일 보내기
"""
import smtplib
import random
from settings import GMAIL_ID, GMAIL_PW


# Context Manager 사용
class MailServer(object):
    def __init__(self, id, pw):
        print("Connect Gmail SMTP server")
        self.smtp_obj = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
        print("Login...", end=" ")
        self.smtp_obj.login(id, pw)
        print(" Complete")

    def __enter__(self):
        return self.smtp_obj

    def __exit__(self, type, value, traceback):
        return self.smtp_obj.quit()


if __name__ == "__main__":
    users = [
        "praga.guest@gmail.com",
        "imdff0803@gmail.com",
        "imdff0803@naver.com",
    ]

    chores = ["dishes", "bathroom", "vacuum", "walk dog"]

    with MailServer(GMAIL_ID, GMAIL_PW) as smtp_obj:
        for user in users:
            chore = random.choice(chores)
            chores.remove(chore)
            smtp_obj.sendmail(
                from_addr=GMAIL_ID,
                to_addrs=user,
                msg=f"Subject: Random Chores\nHello You Should do {chore}"
            )
