#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

USER_AGENT = {'User-agent': 'Mozilla/5.0'}


def searchable_string(user_input):
    """
    replaces any spaces the user input might have to +
    so that it won't interfere with urls
    """
    return user_input.replace(' ', '+')


def search_page(anime_name):
    website_request = Request("http://watch-anime.net/anime-list/search/" +
                              searchable_string(anime_name), None, USER_AGENT)
    website_html = urlopen(website_request).read()
    return website_html


def get_anime_options(html_text):
    li = []
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('h3')
    for i in episode_list:
        episode_urls = i.findAll('a')
        for f in episode_urls:
            li.append(f['href'])
    return li


def get_episodes(html_text):
    """
    This one is odd because it doesn't return a list of episods right away
    it retuns possible animes, so get_episodes() has to go a step further
    to pull the episode urls from all possible anime selections
    """
    li = []
    soup = BeautifulSoup(html_text)
    lu = soup.findAll('li')
    for i in lu:
        a_tag = i.findAll('a')
        for f in a_tag:
            try:
                if len(f['title']) > 3:
                    li.append(f['title'])
            except:
                pass
    return li


def get_episode_urls(html_text):
    """
    This one is odd because it doesn't return a list of episods right away
    it retuns possible animes, so get_episodes() has to go a step further
    to pull the episode urls from all possible anime selections
    """
    li = []
    soup = BeautifulSoup(html_text)
    lu = soup.findAll('li')
    for i in lu:
        a_tag = i.findAll('a')
        for f in a_tag:
            try:
                if len(f['title']) > 3:
                    li.append(f['href'])
            except:
                pass
    return li


def getMirrors(episodeURI):
    li = []
    num = 1
    episodeRequest = Request(episodeURI, None, USER_AGENT)
    episodeHtml = urlopen(episodeRequest).read()
    soup = BeautifulSoup(episodeHtml)
    mirrorList = soup.findAll('div', {'class', 'wpa_tab_ctt'})
    for mirror in mirrorList:
        li.append("Mirror " + str(num))
        num = num + 1
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
    mirrorList = soup.findAll('div', {'class', 'wpa_tab_ctt'})
    for i in mirrorList:
        mirrorUrl = i.findAll('iframe')
        for f in mirrorUrl:
            li.append(f['src'])
    return li


def getHostingSite(mirror):
    """
    due to how this website works, it returns the actual host links when you
    get the mirrors with getMirrorUrls() so for compability with the plugin
    template this method exists but only returns what you pass it without
    touching it
    """
    return mirror


def getNextPrev(currentEpisodeUrl):
    """
    this website has such a horrible way of organizing episodes it may
    not even be worth implementing this method
    """
    pass
