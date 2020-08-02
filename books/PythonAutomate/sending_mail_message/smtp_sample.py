"""smtp_sample.py
smtplib를 사용한 메일 보내기
"""
import smtplib
from email.mime.text import MIMEText
from settings import GMAIL_ID, GMAIL_PW

# SSL 인증을 하는 SMTP 객체 생성
smtp_obj = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)

# 로그인 하기 (235 - 정상코드)
print(smtp_obj.login(GMAIL_ID, GMAIL_PW))

# 메일 보내기 - 한글은 MIMEText 객체를 이용해 변환해야 함
smtp_obj.sendmail(
    from_addr="sender@gmail.com",
    to_addrs="pragma.guest@gmail.com",
    msg=MIMEText("Subject: 안녕하세요.\n파이썬에서 보낸 메일입니다.", "plain").as_string()
)

# 접속 끊기 (221 - 정상코드)
print(smtp_obj.quit())
