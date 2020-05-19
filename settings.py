import env


URL = getattr(env, 'URL', None)
EMAIL_ADDRESSES = getattr(env, 'EMAIL_ADDRESSES', [])
EMAIL_FROM = getattr(env, 'EMAIL_FROM', None)
EMAIL_SUBJECT = getattr(env, 'EMAIL_SUBJECT', "Subject")

ORIGINAL_FILE = 'original_content.html'
FILE_TO_COMPARE = 'content_to_compare.html'

SMTP_HOST = getattr(env, 'SMTP_HOST', "smtp.gmail.com")
SMTP_PORT = getattr(env, 'SMTP_PORT', "25")
SMTP_LOGIN = getattr(env, 'SMTP_LOGIN', "login")
SMTP_PASSWORD = getattr(env, 'SMTP_PASSWORD', "password")