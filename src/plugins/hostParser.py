#!/usr/bin/python3

import re
import ipdb
from os import walk
from os import getcwd
from os.path import splitext


def hostParser(url):

    plugin_list = []
    parser_plugin = None
    final_parser = None
    tmp = None
    # this part creates the list of plugins from the HostParsers directory
    ipdb.set_trace()
    print(getcwd())
    for _, _, plugins in walk('plugins/HostParsers/'):
        for plugin in plugins:
            plugin_list.append(splitext(plugin)[0])

    # this runs through all the modules in the dir and imports the url match
    ipdb.set_trace()
    for plugin in plugin_list:
        if plugin in url and 'cpython' not in plugin:
            tmp = plugin
            parser_plugin = __import__('plugins.HostParsers.' + plugin, globals(),
                                       locals(), [plugin])
    # this iterates through key, val of the vars() dict for parser_plugin
    # when key matches our wanted plugin use its val as a function
    # and return that functions return
    for key, val in vars(parser_plugin).items():
        ipdb.set_trace()
        if tmp == key:
            return val(url)

# for testing purposes only runs if this is executed and not imported
if __name__ == '__main__':
    hostParser('auengine')
