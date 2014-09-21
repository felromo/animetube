#!/usr/bin/python3
import re

def hostParser(url):
    patternList = ["auengine", "trollvid"]
    finalMatch = ""
    content = ""
    for pattern in patternList:
        match = re.findall(pattern, url)
        if match:
            finalMatch = match[0]
    if finalMatch == "auengine":
        from plugins import auengine
        content = auengine.auengine(url)
    if finalMatch == "trollvid":
        from plugins import trollvideo
        content = trollvideo.trollvideo(url)

    return content
