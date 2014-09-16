#!/usr/bin/python3

from .plugins import parser
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
    parser_obj = parser.Parser()
    main_loop = 'd'
    content = ""
    while main_loop != 'q':
        valid = True
        if main_loop == 'd':
            animeName = input("Anime Name: ")
            parser_obj.set_anime(animeName)
            for episode in parser_obj.get_episodes():
                print (episode)
            episode_choice = input("Choose an episode id (number in brackets []): ")
            content = parser_obj.play_episode(int(episode_choice))
        elif main_loop == 'n':
            content = parser_obj.play_episode(parser_obj.next_episode)
        elif main_loop == 'p':
            content = parser_obj.play_episode(parser_obj.next_episode)
        elif main_loop == 'r':
            pass  # don't need to do anything to replay
        else:
            print ("Not a valid option")
            valid = False
        if valid:
            player(content)
        menu()
        main_loop = input(">>")
