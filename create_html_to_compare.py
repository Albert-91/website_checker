import requests

from settings import URL, ORIGINAL_FILE


def download_html_to_file(name):
    content = get_html_content(URL)
    with open("%s" % name, "w") as f:
        f.write(content)


def get_html_content(url):
    r = requests.get(URL)
    return r.text


if __name__ == '__main__':
    download_html_to_file(ORIGINAL_FILE)
