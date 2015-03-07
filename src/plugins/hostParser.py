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
            # break # skip over pyc files with the same name

    # this runs through all the modules in the dir and imports the url match
    for plugin in plugin_list:
        if url in plugin and not 'cpython' in plugin:
            tmp = plugin
            parser_plugin = __import__('HostParsers.' + plugin, globals(),
                                       locals(), [plugin])
    # this needs to call a function from inside the imported module ;-;
    for key, val in vars(parser_plugin).items():
        if tmp == key: # this is not working (plugin is empty)
            return val(url)

if __name__ == '__main__':
    hostParser2('auengine')
