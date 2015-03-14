#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
import re

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def is_multilayered():
    return True


def searchable_string(user_input):
    return quote_plus(user_input)


def search_page(anime_name):
    website_request = Request("http://www.gogoanime.com/?s=" +
                              searchable_string(anime_name), None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_anime_titles(html_text):
    li = []
    li2 = []
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

# after this method runs things can resume like on other plugins..
def get_anime_page(uri):
    website_request = Request(uri, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_episodes(html_text):
    li = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'postlist'})
    for i in episode_list:
        li.append(i.get_text("|").split("|")[4])
    return li


def get_episode_url(html_text):
    li = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'postlist'})
    for i in episode_list:
        episode_url = i.findAll('a')
        for f in episode_url:
            li.append(f['href'])
    return li


def getMirrors(episodeURI):
    li = []
    la = []
    mirrors = []
    pattern = r'(http://)(.+)(\.me|\.net|\.com|\.org)'
    website_request = Request(episodeURI, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    soup = BeautifulSoup(website_html)
    mirror_list = soup.findAll('div', {'class': 'postcontent'})
    for i in mirror_list:
        mirrors = i.findAll('iframe')
        for f in mirrors:
            li.append(f['src'])
    for i in li:
        match = re.search(pattern, i)
        if match is not None:
            sub_str = match.group(2)
            if sub_str[0:5] == "embed":
                la.append(sub_str[6:])
            else:
                la.append(sub_str)
    return la


def getMirrorUrls(episodeURI):
    website_request = Request(episodeURI, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    li = []
    mirrors = []
    soup = BeautifulSoup(website_html)
    mirror_list = soup.findAll('div', {'class': 'postcontent'})
    for i in mirror_list:
        mirrors = i.findAll('iframe')
        for f in mirrors:
            li.append(f['src'])
    return li


def getHostingSite(mirror):
    """due to how this website is handled I think the method should run just like
    getMirrorUrls, since they need to return the same link"""
    website_request = Request(mirror, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    li = []
    mirrors = []
    soup = BeautifulSoup(website_html)
    mirror_list = soup.findAll('div', {'class': 'postcontent'})
    for i in mirror_list:
        mirrors = i.findAll('iframe')
        for f in mirrors:
            li.append(f['src'])
    return li


def getNextPrev(currentEpisodeUrl):
    prevEP = ""
    nextEP = ""
    website_request = Request(currentEpisodeUrl, None, USER_AGENT)
    website_html = urlopen(website_request).read()
    soup = BeautifulSoup(website_html)
    # prev_episode = soup.findAll('div', {'class': 'alignleft'})
    results = soup.findAll('div', {'class': 'alignleft'})
    for i in results:
        tmp = i.findAll('a')
        for f in tmp:
            prevEP = f['href']
    results = soup.findAll('div', {'class': 'alignright'})
    for i in results:
        tmp = i.findAll('a')
        for f in tmp:
            nextEP = f['href']
    return (prevEP, nextEP)
