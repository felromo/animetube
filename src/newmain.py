#!/usr/bin/python3
from plugins import newparser
from subprocess import call, Popen, PIPE, STDOUT
from colorama import Fore, init
import platform
import os

init()  # for windows colorama (will make this os dependent later)

# Just makes it easier to give colors later on in the program
RED = Fore.RED
BLACK = Fore.BLACK
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Fore.RESET

try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')


def menu():
    print (GREEN + "[N]" + RESET + "ext Episode")
    print (GREEN + "[P]" + RESET + "revious Episode")
    print (GREEN + "[D]" + RESET + "ifferent Anime")
    print (GREEN + "[R]" + RESET + "eplay same Episode")
    print (GREEN + "[C]" + RESET + "hange Mirror")
    print (GREEN + "[Q]" + RESET + "uit out of program")


def player(videoContent):
    if platform.system() != "Linux":
        os.putenv('PATH', ';C:\Program Files (x86)\VideoLAN\VLC\;')
        call(['vlc', videoContent, '--play-and-exit'], stdout=DEVNULL, stderr=STDOUT)
    else:
        call(['vlc', videoContent, '--play-and-exit'], stdout=DEVNULL, stderr=STDOUT)

if __name__ == '__main__':
    parser = newparser.parser()
    mainLoop = 'd'
    content = ""
    while mainLoop != 'q':
        valid = True
        if mainLoop == 'd':
            animeName = input("Anime Name: ")
            parser.setAnime(animeName)
            try:
                parser.get_anime_options(animeName)
            except:
                print("Did not have method get_anime_options()")
            else:
                pass
            for selector, episode in parser.getEpisodes():
                print (GREEN + "[" + str(selector) + "]" + RESET + episode)
            episodeChoice = input("Choose an episode id " + GREEN +
                                  "(number in brackets [])" + RESET + ": ")
            content = parser.playEpisode(int(episodeChoice))
        elif mainLoop == 'c':
            for selector, mirror in parser.getMirrors():
                print (GREEN + "[" + str(selector) + "]" + RESET + mirror)
            content = parser.playEpisode(int(episodeChoice),
                                         mirrorChoice=int(input("Mirror: ")))
        elif mainLoop == 'n':
            content = parser.playEpisode(parser.nextEpisode)
            episodeChoice = int(episodeChoice) - 1
            print (episodeChoice)
        elif mainLoop == 'p':
            content = parser.playEpisode(parser.prevEpisode)
            episodeChoice = int(episodeChoice) + 1
            print (episodeChoice)
        elif mainLoop == 'r':
            pass  # don't need to do anything to replay
        else:
            print (RED + "Not a valid option" + RESET)
            valid = False
        if valid:
            print ("Playing: " + parser.getEpisodes()[int(episodeChoice)][1])
            player(content)
        menu()
        mainLoop = input(GREEN + ">>" + RESET)
