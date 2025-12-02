import smtplib
from email.mime.text import MIMEText
import requests
import config

def send_email_alert(msg):
    """
    Send email alert via Gmail SMTP.
    Requires App Password (not regular password).
    """
    try:
        msg_obj = MIMEText(msg)
        msg_obj['Subject'] = '🚨 Geo-Fence Alert'
        msg_obj['From'] = config.EMAIL_FROM
        msg_obj['To'] = config.EMAIL_TO

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config.EMAIL_FROM, config.EMAIL_PASSWORD)
        server.send_message(msg_obj)
        server.quit()
        print("📧 Email sent!")
    except Exception as e:
        print(f"Email Error: {e}")

def telegram_alert(msg, token=config.TELEGRAM_TOKEN, chat_id=config.TELEGRAM_CHAT_ID):
    """
    Send Telegram alert.
    """
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": msg}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("📱 Telegram alert sent!")
    except Exception as e:
        print(f"Telegram Error: {e}")

def sms_alert(msg, number=config.PHONE_NUMBER):
    """
    Send SMS via TextBelt (free: 1/day; paid for more).
    """
    try:
        url = "https://textbelt.com/text"
        data = {"phone": number, "message": msg, "key": "textbelt"}  # Free key
        response = requests.post(url, data=data)
        if response.json().get('success'):
            print("📱 SMS sent!")
        else:
            print("SMS failed (free limit?)")
    except Exception as e:
        print(f"SMS Error: {e}")