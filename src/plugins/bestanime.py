#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def searchable_string(user_input):
    return user_input.replace(' ', '+')


def search_page(anime_name):
    website_request = Request("http://bestanimes.tv/?s=" + searchable_string(anime_name), None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_episodes(html_text):
    li = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_list:
        li.append(i.getText().strip())
    return li


def get_episode_url(html_text):
    li = []
    soup = BeautifulSoup(html_text)
    episode_url_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_url_list:
        episode_url = i.findAll('a')
        for f in episode_url:
            li.append(f['href'])
    return li


def get_mirrors(episode_url):
    """
    Pass it a url and it will return a list with the urls to the
    mirrors of that particular url passed. Will do this for the first element
    in the link passed to it (hard coded as of now will change in future)
    """
    li = []
    episode_request = Request(episode_url, None, USER_AGENT)
    episode_html = urlopen(episode_request).read()
    soup = BeautifulSoup(episode_html)
    mirror_list = soup.findAll('div', {'class', 'sources'})
    for i in mirror_list:
        mirror_url = i.findAll('a')
        for f in mirror_url:
            li.append(f['href'])
    return li


def get_hosting_site(mirror):
    """
    pass it the url of a mirror and it will return the video host provider
    """
    host = ""
    host_request = Request(mirror, None, USER_AGENT)
    host_html = urlopen(host_request)
    soup = BeautifulSoup(host_html)
    host_parse = soup.findAll('div', {'id': 'default', 'class': 'default'})
    for i in host_parse:
        tmp = i.findAll('iframe')
        for f in tmp:
            host = f['src']
    return host
