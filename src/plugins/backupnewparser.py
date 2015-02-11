#!/usr/bin/python3
from plugins import bestanime, hostParser, watch_anime


class parser():
    """
    Wrapper around the actual site parser plugins. This is
    the class that you'll be interacting with instead of
    the actual parsers. This makes it easy to to use any
    plugins while still using the same class and methods.
    """

    def __init__(self, animeName="", action='d', siteParser=bestanime,
                 hostParser='trollvideo'):
        self.animeName = animeName
        self.episodes = None
        self.episodeUrls = None
        self.currentEpisode = None
        self.prevEpisode = None
        self.nextEpisode = None
        self.mirrors = None
        self.mirrorUrls = None
        self.host = None
        self.siteParser = siteParser

    def __setEpisodes(self):
        self.episodes = self.siteParser.get_episodes(
            self.siteParser.search_page(self.animeName))

    def __setEpisodeUrls(self):
        self.episodeUrls = self.siteParser.get_episode_url(
            self.siteParser.search_page(self.animeName))

    def __setMirrors(self, episodeChoice):
        if type(episodeChoice) is int:
            self.mirrors = self.siteParser.getMirrors(self.episodeUrls[episodeChoice])
        else:
            self.mirrors = self.siteParser.getMirrors(episodeChoice)

    def __setMirrorUrls(self, episodeChoice):
        if type(episodeChoice) is int:
            self.mirrorUrls = self.siteParser.getMirrorUrls(self.episodeUrls[episodeChoice])
        else:
            self.mirrorUrls = self.siteParser.getMirrorUrls(episodeChoice)

    def __setHost(self, mirrorChoice):
        # this should change according to a future config file
        self.host = self.siteParser.getHostingSite(self.mirrorUrls[mirrorChoice])

    def __setNextPrev(self, episodeChoice):
        if type(episodeChoice) is int:
            self.prevEpisode, self.nextEpisode = self.siteParser.getNextPrev(
                self.episodeUrls[episodeChoice])
        else:
            self.prevEpisode, self.nextEpisode = self.siteParser.getNextPrev(
                episodeChoice)

    def setAnime(self, animeName):
        self.animeName = self.siteParser.searchable_string(animeName)
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
            # li.append("([{}] {})".format(selector, episode))
            li.append((selector, episode))
            selector = selector + 1
        return li

    def getMirrors(self):
        li = []
        selector = 0
        for mirror in self.mirrors:
            li.append((selector, mirror))
            selector = selector + 1
        return li

    def playEpisode(self, episodeChoice, selection='', mirrorChoice=0):
        """
        this method probably does way more than it should...
        """
        self.__setNextPrev(episodeChoice)
        self.__setMirrors(episodeChoice)
        self.__setMirrorUrls(episodeChoice)
        self.__setHost(mirrorChoice)
        return hostParser.hostParser(self.host)
