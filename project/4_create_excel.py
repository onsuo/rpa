# [선정 명단 엑셀]
# 순번 닉네임 전화번호
# 1 유재석 9429
# 2 박명수 2463
# 3 정형돈 9236

import smtplib
from email.message import EmailMessage

from account import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
)
from imap_tools import MailBox
from openpyxl import Workbook

MAX_VAL = 3  # 최대 선정자 수
applicant_list = []  # 지원자 리스트

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번
    for msg in mailbox.fetch("(SENTSINCE 09-Jan-2023)"):  # 2023년 1월 9일 이후로 온 메일 조회
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print(f"순번: {index}, 닉네임: {nickname}, 전화번호: {phone}")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_  # 수신 메일 주소
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= MAX_VAL:
            title = "파이썬 특강 안내 [선정]"
            content = f"{nickname} 님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {index}번)"
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = f"{nickname} 님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {index - MAX_VAL}번)"

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname, "님에게 메일 발송 완료")

print("[3. 선정자 명단 파일 생성]")
wb = Workbook()
ws = wb.active

ws.append(["순번", "닉네임", "전화번호"])
for applicant in applicant_list[:MAX_VAL]:
    ws.append(applicant[1:])

wb.save("result.xlsx")

print("모든 작업이 완료되었습니다.")
