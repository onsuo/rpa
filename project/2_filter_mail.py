# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
#     (예) 나도코딩/1234

from account import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
)
from imap_tools import MailBox

applicant_list = []  # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번
    for msg in mailbox.fetch("(SENTSINCE 09-Jan-2023)"):  # 2023년 1월 9일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print(f"순번: {index}, 닉네임: {nickname}, 전화번호: {phone}")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)
