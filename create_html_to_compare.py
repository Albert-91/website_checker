import logging

import requests
from requests.exceptions import MissingSchema

from settings import URL, ORIGINAL_FILE_NAME

logger = logging.getLogger(__name__)


def download_html_to_file(url, name):
    try:
        content = get_html_content(url)
    except MissingSchema:
        logger.error("Incorrect URL in your settings.py or env.py.")
    else:
        with open("%s" % name, "w") as f:
            f.write(content)


def get_html_content(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    download_html_to_file(URL, ORIGINAL_FILE_NAME)
