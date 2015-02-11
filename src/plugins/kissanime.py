#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib.parse

USER_AGENT = {'User-agent': 'Mozilla/5.0'}

search = 'baka'

data = urllib.parse.urlencode({'keyboard': search}).encode('ascii')


def searchable_string(user_input):
    return user_input.replace(' ', '+')


def search_page(anime_name):
    website_request = Request("http://kissanime.com/", data, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_episodes(html_text):
    pass


def get_episode_url(html_text):
    pass


def getMirrors(episodeURI):
    pass


def getMirrorUrls(episodeURI):
    pass


def getHostingSie(mirror):
    pass


def getNextPrev(currentEpisodeUrl):
    pass
