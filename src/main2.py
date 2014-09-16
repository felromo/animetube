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
    main_loop = 'd'
    content = ""
    while main_loop != 'q':
        valid = True
        if main_loop == 'd':
            animeName = input("Anime Name: ")
            parser.setAnime(animeName)
            for episode in parser.getEpisodes():
                print (episode)
            episodeChoice = input("Choose an episode id (number in brackets []): ")
            content = parser.playEpisode(int(episodeChoice))
        elif main_loop == 'n':
            content = parser.playEpisode(parser.nextEpisode)
        elif main_loop == 'p':
            content = parser.playEpisode(parser.prevEpisode)
        elif main_loop == 'r':
            pass  # don't need to do anything to replay
        else:
            print ("Not a valid option")
            valid = False
        if valid:
            player(content)
        menu()
        main_loop = input(">>")
