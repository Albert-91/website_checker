import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template

from settings import EMAIL_ADDRESSES, EMAIL_FROM, EMAIL_SUBJECT


def send_email():
    try:
        s = smtplib.SMTP(host=os.environ.get('SMTP_HOST'), port=os.environ.get('SMTP_PORT'))
        s.starttls()
        s.login(os.environ.get('SMTP_LOGIN'), os.environ.get('SMTP_PASSWORD'))
        for email in EMAIL_ADDRESSES:
            msg = create_msg(email)
            s.send_message(msg)
            del msg
    except Exception as e:
        print(e)
    finally:
        s.quit()


def create_msg(email_to):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = email_to
    message = read_template('email_template.html')
    msg.attach(MIMEText(message.template, 'html'))
    return msg


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
