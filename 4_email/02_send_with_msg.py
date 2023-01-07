import smtplib
from email.message import EmailMessage

from account import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
)

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = EMAIL_ADDRESS  # 받는 사람

# 여러 명에게 메일을 보낼 때
msg["To"] = "jaewon.rhea@gmail.com, jaewon.rhea@gmail.com"
to_list = [EMAIL_ADDRESS, EMAIL_ADDRESS]
msg["To"] = ", ".join(to_list)

# 참조
msg["Cc"] = EMAIL_ADDRESS

# 비밀 참조
msg["Bcc"] = EMAIL_ADDRESS

msg.set_content("테스트 본문입니다.")  # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
