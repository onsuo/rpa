import datetime
import time

from account import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
)
from imap_tools import MailBox

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기
    for msg in mailbox.fetch():
        print(f"[{msg.from_}] {msg.subject}")

    # 읽지 않은 메일
    for msg in mailbox.fetch("(UNSEEN)", reverse=True):
        print(f"[{msg.from_}] {msg.subject}")

    # 특정인이 보낸 메일
    for msg in mailbox.fetch("(FROM jaewon.rhea@gmail.com)"):
        print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자를 포함하는 메일 (제목, 본문)
    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸기
    for msg in mailbox.fetch('(TEXT "test mail")'):  # test, mail 이 포함된 메일 검색
        print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자를 포함하는 메일 (제목만)
    for msg in mailbox.fetch('(SUBJECT "test mail")'):
        print(f"[{msg.from_}] {msg.subject}")

    # 어떤 글자(한글)을 포함하는 메일 필터링 (제목만)
    for msg in mailbox.fetch(limit=5, reverse=True):
        if "테스트" in msg.subject:
            print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜 이후의 메일
    for msg in mailbox.fetch("(SENTSINCE 07-Jan-2023)", reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")

    # 특정 날짜에 온 메일
    for msg in mailbox.fetch("(ON 07-Jan-2023)", reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")

    date = time.strftime("%d-%a-%Y")  # 현재 날짜를 일-요일-연도
    print(date)
    DATE = "2023-01-07"
    dt = datetime.datetime.strptime(DATE, "%Y-%m-%d")
    date = dt.strftime("%d-%b-%Y")
    print(date)
    for msg in mailbox.fetch(f"(ON {date})", reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건을 모두 만족하는 메일 (그리고 조건)
    for msg in mailbox.fetch('(ON 07-Jan-2023 SUBJECT "test mail")', reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (또는 조건)
    for msg in mailbox.fetch('(OR ON 07-Jan-2023 SUBJECT "test mail")', reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")
