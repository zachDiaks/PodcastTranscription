'''
Transcribe all episodes of a podcast. Check your AssemblyAI dashboard for status.
'''
import sys
import transcribeEpsidoe as Transcriber
import getEpisodeLinks as Getter

def transcribeAllEpisodes(url):
    # Get all podcast episode URLs for the MP3
    episodeLinks = Getter.parseFeed(url)

    # Transcribe audio for each in a loop
    for episode in episodeLinks:
        id = Transcriber.batchTranscribeEpisode(episode)
        print(id)

if __name__ == "__main__":
    url = sys.argv[1]
    transcribeAllEpisodes(url)