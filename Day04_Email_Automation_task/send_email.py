import smtplib
from email.message import EmailMessage
import pandas as pd

EMAIL = "xyz@gmail.com"
PASSWORD = "xxxx xxxx xxxx xxxx"


def send_email(receiver, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = receiver
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print(f"Sent to {receiver} ✅")


# 📄 Read CSV
data = pd.read_csv("emails.csv")

# 📄 Read message template
with open("message.txt", "r") as file:
    template = file.read()

# 🔁 Loop through each user
for index, row in data.iterrows():
    name = row['name']
    email = row['email']

    # Replace {name} in template
    message = template.replace("{name}", name)

    send_email(email, "Automated Email", message)