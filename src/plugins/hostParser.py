#!/usr/bin/python3

import re
from os import walk
from os.path import splitext


def hostParser(url):

    plugin_list = []
    parser_plugin = None
    final_parser = None
    tmp = None
    # this part creates the list of plugins from the HostParsers directory
    for _, _, plugins in walk('./HostParsers'):
        for plugin in plugins:
            plugin_list.append(splitext(plugin)[0])

    # this runs through all the modules in the dir and imports the url match
    for plugin in plugin_list:
        if url in plugin and 'cpython' not in plugin:
            tmp = plugin
            parser_plugin = __import__('HostParsers.' + plugin, globals(),
                                       locals(), [plugin])
    # this iterates through key, val of the vars() dict for parser_plugin
    # when key matches our wanted plugin use its val as a function
    # and return that functions return
    for key, val in vars(parser_plugin).items():
        if tmp == key:
            return val(url)

# for testing purposes only runs if this is executed and not imported
if __name__ == '__main__':
    hostParser('auengine')
