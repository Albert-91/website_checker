import filecmp

from email_sender.email_sender import send_email
from settings import ORIGINAL_FILE, FILE_TO_COMPARE
from create_html_to_compare import download_html_to_file


def check_website():
    download_html_to_file(FILE_TO_COMPARE)
    if not filecmp.cmp(ORIGINAL_FILE, FILE_TO_COMPARE, shallow=True):
        send_email()


if __name__ == '__main__':
    check_website()
