import filecmp
import logging

from create_html_to_compare import download_html_to_file
from email_sender.email_sender import send_email
from settings import ORIGINAL_FILE, FILE_TO_COMPARE

logger = logging.getLogger(__name__)


def check_website():
    download_html_to_file(FILE_TO_COMPARE)
    try:
        if not filecmp.cmp(ORIGINAL_FILE, FILE_TO_COMPARE, shallow=True):
            send_email()
    except FileNotFoundError:
        logger.error("%s file was not found. Firstly create it by running script 'create_html_to_compare.py'" % ORIGINAL_FILE)


if __name__ == '__main__':
    check_website()
