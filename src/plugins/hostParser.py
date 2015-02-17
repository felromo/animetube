#!/usr/bin/python3
import re


def hostParser(url):
    patternList = ["auengine", "easyvideo", "mp4upload", "playbb", "trollvid",
                   "video44", "videofun", "videowing", "vidzur", "yucache"]
    finalMatch = ""
    content = ""
    for pattern in patternList:
        match = re.findall(pattern, url)
        if match:
            finalMatch = match[0]
    if finalMatch == "auengine":
        from plugins import auengine
        content = auengine.auengine(url)
    if finalMatch == "easyvideo":
        from plugins import easyvideo
        content = easyvideo.easyvideo(url)
    if finalMatch == "mp4upload":
        from plugins import mp4upload
        content = mp4upload.mp4upload(url)
    if finalMatch == "playbb":
        from plugins import playbb
        content = playbb.playbb(url)
    if finalMatch == "trollvid":
        from plugins import trollvideo
        content = trollvideo.trollvideo(url)
    if finalMatch == "video44":
        from plugins import video44
        content = video44.video44(url)
    if finalMatch == "videofun":
        from plugins import videofun
        content = videofun.videofun(url)
    if finalMatch == "videowing":
        from plugins import videowing
        content = videowing.videowing(url)
    if finalMatch == "vidzur":
        from plugins import vidzur
        content = vidzur.vidzur(url)
    if finalMatch == "yucache":
        from plugins import yucache
        content = yucache.yucache(url)

    return content
