#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import quote_plus

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def searchable_string(user_input):
    """method takes in a string, then replaces all the spaces with + and
    returns a new string"""
    return quote_plus(user_input)


def search_page(anime_name):
    """makes a request to the search function on the site and returns
    that html"""
    website_request = Request("http://bestanimes.tv/?s=" +
                              searchable_string(anime_name), None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_episodes(html_text):
    """parses the passed parameter and looks for the episodes title (the text)"""
    li = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_list:
        # print(i.getText().strip())
        li.append(i.getText().strip())
    return li


def get_episode_url(html_text):
    """parses the passed parameter and looks for the episodes title (the link)"""
    li = []
    soup = BeautifulSoup(html_text)
    episode_url_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_url_list:
        episode_url = i.findAll('a')
        for f in episode_url:
            li.append(f['href'])
    return li


def getMirrors(episodeURI):
    li = []
    episodeRequest = Request(episodeURI, None, USER_AGENT)
    episodeHtml = urlopen(episodeRequest).read()
    soup = BeautifulSoup(episodeHtml)
    mirrorList = soup.findAll('div', {'class', 'sources'})
    for mirror in mirrorList:
        li.append(mirror.get_text())
    return li


def getMirrorUrls(episodeURI):
    """
    Pass it a url and it will return a list with the urls to the
    mirrors of that particular url passed. Will do this for the first element
    in the link passed to it (hard coded as of now will change in future)
    """
    li = []
    episodeRequest = Request(episodeURI, None, USER_AGENT)
    episodeHtml = urlopen(episodeRequest).read()
    soup = BeautifulSoup(episodeHtml)
    mirrorList = soup.findAll('div', {'class', 'sources'})
    for i in mirrorList:
        mirrorUrl = i.findAll('a')
        for f in mirrorUrl:
            li.append(f['href'])
    return li


def getHostingSite(mirror):
    """
    pass it the url of a mirror and it will return the video host provider
    """
    host = ""
    hostRequest = Request(mirror, None, USER_AGENT)
    hostHtml = urlopen(hostRequest)
    soup = BeautifulSoup(hostHtml)
    hostParse = soup.findAll('div', {'id': 'default', 'class': 'default'})
    for i in hostParse:
        tmp = i.findAll('iframe')
        for f in tmp:
            host = f['src']
    return host


def getNextPrev(currentEpisodeUrl):
    """
    pass it the url of the currently viewed episode, and it will return a
    touple containing (previous episode, next episode)
    """
    prevEP = ""
    nextEP = ""
    pageRequest = Request(currentEpisodeUrl, None, USER_AGENT)
    pageHtml = urlopen(pageRequest).read()
    soup = BeautifulSoup(pageHtml)
    results = soup.findAll('div', {'class': 'floatLeft'})
    for i in results:
        tmp = i.findAll('a')
        for f in tmp:
            prevEP = f['href']
    results = soup.findAll('div', {'class': 'floatRight'})
    for i in results:
        tmp = i.findAll('a')
        for f in tmp:
            nextEP = f['href']
    return (prevEP, nextEP)
