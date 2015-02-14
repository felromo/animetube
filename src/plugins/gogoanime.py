#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib.parse
import re

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def is_multilayered():
    return True


def searchable_string(user_input):
    return user_input.replace(' ', '+')


def search_page(anime_name):
    website_request = Request("http://www.gogoanime.com/?s=" +
                              searchable_string(anime_name), None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_anime_titles(html_text):
    li = []
    li2 = []
    content = []
    pattern = r'category'
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'postlist'})
    for link in episode_list:
        episode_url = link.findAll('a')
        for f in episode_url:
            li2.append(f['href'])
            match = re.search(pattern, f['href'])
            if match is not None:
                li.append(f.get_text())
    return li


def get_anime_urls(html_text):
    li = []
    pattern = r'category'
    content = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'postlist'})
    for i in episode_list:
        episode_url = i.findAll('a')
        for f in episode_url:
            li.append(f['href'])
    for test in li:
        match = re.search(pattern, test)
        if match is not None:
            content.append(match.string)
    return content


def get_anime_page(uri):
    website_request = Request(uri, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_episodes(html_text):
    li = []
    content = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'postlist'})
    for i in episode_list:
        li.append(i.get_text("|").split("|")[4])
    return li


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
