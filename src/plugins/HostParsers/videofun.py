#!/usr/bin/python3
import re
from urllib.request import urlopen, Request
from urllib.parse import unquote
from bs4 import BeautifulSoup

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def videofun(hostUrl):
    """
    takes in a link with the embeded video player and returns a clean url of
    the actual content to be passed onto the player
    """
    content = ""
    pattern = r'url:\s*\"(.+)\"'
    videoRequest = Request(hostUrl, None, USER_AGENT)
    videoHtml = urlopen(videoRequest).read()
    soup = BeautifulSoup(videoHtml)
    scripts = soup.findAll('script', {'type': 'text/javascript'})
    script = scripts[-1]
    for line in script:
        match = re.findall(pattern, line)
        content = match[-1]
        # content.split(",")
    return unquote(content.split(",")[0][:-1])
