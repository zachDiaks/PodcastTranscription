'''
From an RSS feed URL, find all of the MP3 links to the episodes in the podcast
'''
import sys
import re
import requests

def parseFeed(url):
    resp = requests.get(url)
    html = resp.text
    links = re.findall('url=(.*mp3)',html)
    return [link.replace('\'','').replace('"','') for link in links]

if __name__ == "__main__":
    url = sys.argv[1]
    print(parseFeed(url))