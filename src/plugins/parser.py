#!/usr/bin/python3
from . import bestanime, trollvideo

class Parser():

    def __init__(self, anime_name="", action='d', siteParser='bestanime',
                 hostParser='trollvideo'):
        self.anime_name = anime_name
        self.episodes = []
        self.episode_urls = None
        self.prev_episode = None
        self.next_episode = None
        self.mirrors = None
        self.host = None


    def __set_episodes(self):
        self.episodes = bestanime.get_episodes(bestanime.search_page(self.anime_name))

    def __set_episode_urls(self):
        self.episode_urls = bestanime.get_episode_url(bestanime.search_page(self.anime_name))

    def __set_mirrors(self, episode_choice):
        if type(episode_choice) is int:
            self.mirrors = bestanime.get_mirrors(self.episode_urls[episode_choice])
        else:
            self.mirrors = bestanime.get_mirrors(episode_choice)

    def __set_host(self):
        # this should change according to a future config file
        self.host = bestanime.get_hosting_site(self.mirrors[0])

    def __set_next_prev(self, episode_choice):
        #TODO
        if type(episode_choice) is int:
            self.prev_episode, self.next_episode = bestanime.getNextPrev(self.episode_urls[episode_choice])
        else:
            self.prev_episode, self.next_episode = bestanime.getNextPrev(episode_choice)

    def set_anime(self, anime_name):
        self.anime_name = bestanime.searchable_string(anime_name)
        self.__set_episodes()
        self.__set_episode_urls()

    def get_episodes(self):
        li = []
        selector = 0
        for episode in self.episodes:
            li.append("([{}] {})".format(selector, episode))
            selector = selector + 1
        return li

    def play_episode(self, episode_choice, selection=''):
        self.__set_next_prev(episode_choice)
        self.__set_mirrors(episode_choice)
        self.__set_host()
        return trollvideo.trollvideo(self.host)






