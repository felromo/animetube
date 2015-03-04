#!/usr/bin/python3
import re
from urllib.request import urlopen, Request
from urllib.parse import unquote
from bs4 import BeautifulSoup

USER_AGENT = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.22280 Safari/537.36'}


def trollvideo(hostUrl):
    """
    takes in a link with the embeded video player and returns a clean url of
    the actual content to be passed onto the player
    """

    content = ""
    search_pattern = r'file:\s(.+)'
    videoRequest = Request(hostUrl, None, USER_AGENT)
    videoHtml = urlopen(videoRequest).read()
    soup = BeautifulSoup(videoHtml)
    scripts = soup.findAll('script', {'type': 'text/javascript'})
    script = scripts[-2]
    for line in script:
        match = re.search(search_pattern, line)
        content = match.group(1)
    return unquote(content[1:-2])

