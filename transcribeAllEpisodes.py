'''
Transcribe all episodes of a podcast. Check your AssemblyAI dashboard for status.
'''
import sys
import os
from Transcriber import Transcriber
from PodcastUtils import PodcastUtils

def transcribeAllEpisodes(url,fname):
    # Create classes
    t = Transcriber(os.environ['AAI_API_KEY'])
    pu = PodcastUtils()

    # Get all podcast episode URLs for the MP3
    episodeLinks = pu.episodeLinks(url)

    # Transcribe audio for each in a loop
    numEpisodes = len(episodeLinks)
    ids = [0] * numEpisodes
    c = 0
    for episode in episodeLinks:
        ids[c] = t.submitTranscription(episode)
        c += 1
    
    # Write transcriptions to a file
    with open(fname,'w') as f:
        for id in ids:
            f.writeline(id)

if __name__ == "__main__":
    url = sys.argv[1]
    fname = sys.argv[2]
    transcribeAllEpisodes(url,fname)