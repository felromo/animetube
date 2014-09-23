#!/usr/bin/python3
import re


def hostParser(url):
    patternList = ["auengine", "trollvid", "mp4upload"]
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
    if finalMatch == "mp4upload":
        from plugins import mp4upload
        content = mp4upload.mp4upload(url)

    return content
