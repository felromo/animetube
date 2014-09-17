#!/usr/bin/python3
import re
from urllib.request import urlopen, Request
from urllib.parse import unquote
from bs4 import BeautifulSoup

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def auengine(host_url):
    """
    takes in a link with the embeded video player and returns a clean url of
    the actual content to be passed onto the player
    """
    content = ""
    pattern = r'url:\s*\'(.+)\''
    video_request = Request(host_url, None, USER_AGENT)
    video_html = urlopen(video_request).read()
    soup = BeautifulSoup(video_html)
    scripts = soup.findAll('script', {'type': 'text/javascript'})
    script = scripts[2]
    for line in script:
        match = re.findall(pattern, line)
        content = match
    return unquote(content[-1])
