import os
import logging

logger = logging.getLogger()

Max_file_size = 2000000
email_sender = "Amazon.Returns.Department@gmail.com"
email_receiver = "Amazon.Returns.Department@gmail.com"
cc_emails = ""
password = "Amazon19?Returns12"

def send_email(subject, body):
    import smtplib
    from smtplib import SMTPException
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email import encoders

    sender_email = email_sender
    receiver_email = email_receiver
    ccc_emails = cc_emails
    to_emails = receiver_email.split(',') + ccc_emails.split(',')

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message['CC'] = ccc_emails
    message.attach(MIMEText(body, 'html'))
    text = message.as_string()

    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(sender_email, password)
        smtpobj.sendmail(sender_email, to_emails, text)
        smtpobj.close()
    except SMTPException:
        logger.exception(f"Unable to send email. Failed to send from {sender_email} to {','.join(to_emails)}.")

