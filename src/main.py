#!/usr/bin/python3
from plugins import bestanime, trollvideo
from subprocess import call, Popen, PIPE, STDOUT

try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


def animeName():
    animeName = input("Type an anime name: ")
    return bestanime.searchable_string(animeName)


def parser(animeName, action='d'):
    print (action)
    parser.episodes = bestanime.get_episodes(bestanime.search_page(animeName))
    episodeUrls = bestanime.get_episode_url(bestanime.search_page(animeName))
    selector = 0
    for episode in parser.episodes:
        print ("([{}] {})".format(selector, episode))
        selector = selector + 1

    if action != "n" and action != "p":
        parser.episodeChoice = input("Choose an episode to view: ")
    elif action == "n":
        parser.episodeChoice = int(parser.episodeChoice) - 1
    elif action == "p":
        parser.episodeChoice = int(parser.episodeChoice) + 1
    print ("Viewing ", parser.episodes[int(parser.episodeChoice)])

    mirrors = bestanime.getMirrors(episodeUrls[int(parser.episodeChoice)])
    prevEpisode, nextEpisode = bestanime.getNextPrev(
        episodeUrls[int(parser.episodeChoice)])
    print ("Available Mirrors")
    print (mirrors)

    host = bestanime.getHostingSite(mirrors[0])
    if action == 'n':
        host = bestanime.getHostingSite(nextEpisode)
    if action == 'p':
        host = bestanime.getHostingSite(prevEpisode)
    print (host)

    content = trollvideo.trollvideo(host)
    return content


def player(videoContent):
    call(['vlc', videoContent, '--play-and-exit'], stdout=DEVNULL,
         stderr=STDOUT)

    print ("Video has finished")


def menu():
    print ("[N]ext Episode")
    print ("[P]revious Episode")
    print ("[D]ifferent Anime")
    print ("[R]eplay same Episode")
    print ("[Q]uit out of program")

if __name__ == "__main__":
    menuChoice = 'd'
    while menuChoice != 'q':
        if menuChoice == 'd':
            animename = animeName()
        videoContent = parser(animename, action=menuChoice)
        player(videoContent)
        menu()
        menuChoice = input(">>")
