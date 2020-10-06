import filecmp
import logging

from create_html_to_compare import download_html_to_file
from email_sender.email_sender import send_email
from settings import (
    ORIGINAL_FILE_NAME,
    FILE_TO_COMPARE_NAME,
    CHECKING_ON_DIFFS_ENABLED,
    CHECKING_ON_PHRASES_ENABLED,
    CHECKING_ON_DIFFS_EMAIL_TEMPLATE,
    CHECKING_ON_PHRASES_EMAIL_TEMPLATE,
    CHECKING_ON_PHRASES_PHRASES, URL
)

logger = logging.getLogger(__name__)


def check_website():
    download_html_to_file(URL, FILE_TO_COMPARE_NAME)
    if CHECKING_ON_DIFFS_ENABLED:
        try:
            if not filecmp.cmp(ORIGINAL_FILE_NAME, FILE_TO_COMPARE_NAME, shallow=True):
                send_email(CHECKING_ON_DIFFS_EMAIL_TEMPLATE)
        except FileNotFoundError:
            logger.error("%s file was not found. Firstly create it by running script 'create_html_to_compare.py'" % ORIGINAL_FILE_NAME)
    if CHECKING_ON_PHRASES_ENABLED:
        with open(FILE_TO_COMPARE_NAME) as f:
            for phrase in CHECKING_ON_PHRASES_PHRASES:
                if phrase in f.read():
                    send_email(CHECKING_ON_PHRASES_EMAIL_TEMPLATE)


if __name__ == '__main__':
    check_website()
