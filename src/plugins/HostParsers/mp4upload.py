#!/usr/bin/python3
import re
from urllib.request import urlopen, Request
from urllib.parse import unquote
from bs4 import BeautifulSoup

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def mp4upload(hostUrl):
    """
    takes in a link with the embeded video player and returns a clean url of
    the actual content to be passed onto the player
    """
    content = ""
    search_pattern = r'.+file.+:\s*(.+)'
    videoRequest = Request(hostUrl, None, USER_AGENT)
    videoHtml = urlopen(videoRequest).read()
    soup = BeautifulSoup(videoHtml)
    scripts = soup.findAll('script', {'type': 'text/javascript'})
    script = scripts[-2]
    for line in script:
        match = re.search(search_pattern, line)
        content = match.group(1)
    content = "http://www9.mp4upload.com:" + content
    return unquote(content[:-2])

    """
    script = scripts[-2]
    for line in script:
        match = re.search(pattern, line)
        content = match.group(1)
    return unquote(content)
    """
