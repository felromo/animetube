#/usr/bin/python3

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
    soup = BeautifulSoup(html_text)
    episode_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_list:
        print(i.getText().strip())

def get_episode_url(html_text):
    soup = BeautifulSoup(html_text)
    episode_url_list = soup.findAll('div', {'class': 'episode-list'})
    for i in episode_url_list:
        episode_url = i.findAll('a')
        for f in episode_url:
            print(f['href'])
