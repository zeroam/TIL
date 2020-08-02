"""ezgmail_sample.py
ezgmail 라이브러리 활용
"""
import ezgmail

# 인증 진행
ezgmail.init()

# 인증된 이메일 주소 출력
print(f"내 이메일 주소: {ezgmail.EMAIL_ADDRESS}")

# 메일 보내기
ezgmail.send(
    recipient="pragma.guest@gmail.com", # 받는이
    subject="Subject line",             # 주제문
    body="Body of the email",           # 본문
    attachments=["attachment.txt"],     # 첨부 파일들
    cc=None,                            # 참조
    bcc=None,                           # 비밀참조
)

# 읽지 않은 메일 확인하기
unread_threads = ezgmail.unread()  # GmailThread 객체 리스트 반환
ezgmail.summary(unread_threads)

# 메일 속성 접근하기
print(f"안 읽은 메일 갯수: {len(unread_threads)}")
unread = unread_threads[0]
print(f"GmailThread 문자열 값: {unread}")
print(f"안 읽은 첫 번째 메일의 메시지 갯수: {len(unread.messages)}")
print(f"  메시지 주제문: {unread.messages[0].subject}")
print(f"  메시지 본문: {unread.messages[0].body}")
print(f"  메시지 시간: {unread.messages[0].timestamp}")
print(f"  메시지 보낸이: {unread.messages[0].sender}")
print(f"  메시지 받는이: {unread.messages[0].recipient}")

# 최근 받은 메일 확인 (기본 25)
recent_threads = ezgmail.recent(maxResults=100)
print(f"최근 받은 메일 갯수: {len(recent_threads)}")

# 검색 기능 활용하기
result_threads = ezgmail.search("has:attachment")
print(f"첨부 파일이 있는 메일:")
ezgmail.summary(result_threads)

# 첨부 파일 다운로드
thread = result_threads[0]
print(f"첨부 파일: {thread.messages[0].attachments}")
thread.messages[0].downloadAttachment("attachment.txt")  # 첨부파일 하나 다운로드
thread.messages[0].downloadAllAttachments(downloadFolder="attach")  # 첨부파일 모두 다운로드
