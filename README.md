# Website checker

## Description
Script was created to follow website which you want to be followed. For example if I am waiting for changes on some 
website, I can create one HTML copy of this website and then run this script in CRON to run for example everyday. Script 
creates copy and then compares original HTML which you have created with this HTML created by script. If there is some 
changes then e-mail is sending to recipient from settings or env file.

## Procedures
1. Create file which will be compared `original_content.html` by command:
    ```bash
    python3 create_html_to_compare.py
    ```
1. Create `env.py` file with all SMTP credentials and some e-mail settings. Here is some example:
    ```python
    URL = "https://some_url.com"
    EMAIL_ADDRESSES = [
        'address1@example.com',
        'address2@example.com',
    ]
    EMAIL_FROM = 'address@example.com'
    EMAIL_SUBJECT = "Website has changed!"
    
    SMTP_HOST = 'smtp.example.com'
    SMTP_PORT = '587'
    SMTP_LOGIN = 'login'
    SMTP_PASSWORD = 'password'
    ```
1. Create your own copy of email template with name `email_to_send.html`
