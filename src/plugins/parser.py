#!/usr/bin/python3
from plugins import bestanime, trollvideo


class parser():

    def __init__(self, animeName="", action='d', siteParser='bestanime',
                 hostParser='trollvideo'):
        self.animeName = animeName
        self.episodes = None
        self.episodeUrls = None
        self.currentEpisode = None
        self.prevEpisode = None
        self.nextEpisode = None
        self.mirrors = None
        self.host = None

    def __setEpisodes(self):
        self.episodes = bestanime.get_episodes(
            bestanime.search_page(self.animeName))

    def __setEpisodeUrls(self):
        self.episodeUrls = bestanime.get_episode_url(
            bestanime.search_page(self.animeName))

    def __setMirrors(self, episodeChoice):
        if type(episodeChoice) is int:
            self.mirrors = bestanime.getMirrors(self.episodeUrls[episodeChoice])
        else:
            self.mirrors = bestanime.getMirrors(episodeChoice)

    def __setHost(self):
        # this should change according to a future config file
        self.host = bestanime.getHostingSite(self.mirrors[0])

    def __setNextPrev(self, episodeChoice):
        if type(episodeChoice) is int:
            self.prevEpisode, self.nextEpisode = bestanime.getNextPrev(
                self.episodeUrls[episodeChoice])
        else:
            self.prevEpisode, self.nextEpisode = bestanime.getNextPrev(
                episodeChoice)

    def setAnime(self, animeName):
        self.animeName = bestanime.searchable_string(animeName)
        self.__setEpisodes()
        self.__setEpisodeUrls()

    def getEpisodes(self):
        """
        maybe make this return a touple with selector, episode
        or a dictionary ? key:selector value:touple(episode,url)
        """
        li = []
        selector = 0
        for episode in self.episodes:
            li.append("([{}] {})".format(selector, episode))
            selector = selector + 1
        return li

    def playEpisode(self, episodeChoice, selection=''):
        self.__setNextPrev(episodeChoice)
        self.__setMirrors(episodeChoice)
        self.__setHost()
        return trollvideo.trollvideo(self.host)
