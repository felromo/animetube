#!/usr/bin/python3
from plugins import parser
from subprocess import call, Popen, PIPE, STDOUT

try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


def menu():
    print ("[N]ext Episode")
    print ("[P]revious Episode")
    print ("[D]ifferent Anime")
    print ("[R]eplay same Episode")
    print ("[Q]uit out of program")


def player(videoContent):
    call(['vlc', videoContent, '--play-and-exit'], stdout=DEVNULL,
         stderr=STDOUT)

if __name__ == '__main__':
    parser = parser.parser()
    mainLoop = 'd'
    content = ""
    while mainLoop != 'q':
        valid = True
        if mainLoop == 'd':
            animeName = input("Anime Name: ")
            parser.setAnime(animeName)
            for episode in parser.getEpisodes():
                print (episode)
            episodeChoice = input("Choose an episode id (number in brackets []): ")
            content = parser.playEpisode(int(episodeChoice))
        elif mainLoop == 'n':
            content = parser.playEpisode(parser.nextEpisode)
        elif mainLoop == 'p':
            content = parser.playEpisode(parser.prevEpisode)
        elif mainLoop == 'r':
            pass  # don't need to do anything to replay
        else:
            print ("Not a valid option")
            valid = False
        if valid:
            print ("Playing: " + parser.getEpisodes()[int(episodeChoice)][5:-1])
            player(content)
        menu()
        mainLoop = input(">>")
