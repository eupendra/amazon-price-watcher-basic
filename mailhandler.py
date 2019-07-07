import smtplib
import config

def sendmail(subject, body):
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.USER_NAME, config.USER_PASS)
    message_body = f"Subject:{subject}\n\n{body}"
    smtp.sendmail(config.USER_NAME, config.USER_NAME,message_body)
    smtp.quit()

