"""imap_sample.py
imapclient를 이용한 메일 확인,
pyzmail을 통한 포맷 변환
"""
import imapclient
import pyzmail

from settings import GMAIL_ID, GMAIL_PW

# Gmail 로그인
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap_obj.login(GMAIL_ID, GMAIL_PW)

# 2020년 7월 5일 이후 메일 확인
imap_obj.select_folder("INBOX", readonly=True)
uids = imap_obj.search(["SINCE", "05-Jul-2020"])
print(f"UIDs: {uids}")

# 첫 번째 메일 fetch
raw_messages = imap_obj.fetch([uids[0]], ["BODY[]", "FLAGS"])
message = pyzmail.PyzMessage.factory(raw_messages[uids[0]][b"BODY[]"])
print(f"제목: {message.get_subject()}")  # 제목 출력
print(f"보낸이: {message.get_address('from')}")
print(f"받는이: {message.get_address('to')}")
print(f"참조: {message.get_address('cc')}")
print(f"비밀참조: {message.get_address('bcc')}")

if message.text_part != None:
    print("텍스트:")
    print(message.text_part.get_payload().decode(message.text_part.charset))

if message.html_part != None:
    print("HTML:")
    print(message.html_part.get_payload().decode(message.html_part.charset))

# 로그아웃
imap_obj.logout()
