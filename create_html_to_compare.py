import logging

import requests
from requests.exceptions import MissingSchema

from settings import URL, ORIGINAL_FILE_NAME

logger = logging.getLogger(__name__)


def download_html_to_file(name):
    try:
        content = get_html_content(URL)
    except MissingSchema:
        logger.error("Incorrect URL in your setteings.py or env.py.")
    else:
        with open("%s" % name, "w") as f:
            f.write(content)


def get_html_content(url):
    r = requests.get(URL)
    return r.text


if __name__ == '__main__':
    download_html_to_file(ORIGINAL_FILE_NAME)
