import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

from settings import EMAIL_ADDRESSES, EMAIL_FROM, EMAIL_SUBJECT, SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_LOGIN

logger = logging.getLogger(__name__)


def send_email():
    try:
        s = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
        s.starttls()
        s.login(SMTP_LOGIN, SMTP_PASSWORD)
        for email in EMAIL_ADDRESSES:
            msg = create_msg(email)
            s.send_message(msg)
            del msg
            logger.debug("E-mail sent.")
    except Exception as e:
        logger.error(e)
    finally:
        s.quit()


def create_msg(email_to):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = email_to
    message = read_template(Path('email_sender/email_template.html'))
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
