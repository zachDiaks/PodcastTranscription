'''
PodcastUtils: Utility class for working with podcast data
'''
import re
import requests 

class PodcastUtils:
    # Constructor
    def __init__(self):
        pass

    # Grab episode links from RSS feed
    def episodeLinks(self,feed):
        resp = requests.get(feed)
        html = resp.text
        links = re.findall('url=(.*mp3)',html)
        return [link.replace('\'','').replace('"','') for link in links]