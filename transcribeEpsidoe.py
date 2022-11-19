'''
transcribeEpisode: Get the transcription of a podcast episode by passing a link to the hosted MP3 file. 
This script will wait until the transcription is ready, will write the transcription to a file in a folder underneath your working directory named "transcriptions".
Inputs:
    - url: The URL to the MP3 file for the podcast. You can find this using https://www.listennotes.com/ , looking at the RSS xml file, searching for .mp3
'''
import requests
import os
import sys
import checkTranscriptionStatus as StatusChecker
import time

def transcribeEpisode(url):
    # Submit the request
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": url
    }
    headers = {
        "authorization": os.environ['AAI_API_KEY'],
        "content-type": "application/json",
        "speaker_labels": True
    }
    initialResponse = requests.post(endpoint, json=json, headers=headers)
    print("Request for %s submitted"%url)
    print(initialResponse)
    print("Waiting for transcription to finish...")
    jsonResponse = initialResponse.json()
    id = jsonResponse['id']
    statusResponse = StatusChecker.checkStatus(id)
    while(not statusResponse['status'] == 'completed'):
        # Sleep for 2 minutes
        time.sleep(60*2)
        # Check the response again
        statusResponse = StatusChecker.checkStatus(id)
    
    # At this point, the transcription should be complete. Now, let's write the transcription to a file
    transcript = statusResponse['text']
    if not os.path.exists('Transcriptions'):
        


if __name__ == "__main__":
    url = sys.argv[1]
    transcribeEpisode(url)