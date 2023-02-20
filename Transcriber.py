'''
Transcriber: utility class for submitting transcriptions to AssemblyAI
'''
import os
import requests

class Transcriber:
    # Constructor
    def __init__(self,apikey):
        self.apikey = apikey

    # Submit transcription to AssemblyAI, return the transcription ID to be used later
    def submitTranscription(self,url):
        # Create the request header
        endpoint = "https://api.assemblyai.com/v2/transcript"
        json = {
            "audio_url": url,
            "speaker_labels": True
        }
        headers = {
            "authorization": self.apikey,
            "content-type": "application/json"
        }
        initialResponse = requests.post(endpoint, json=json, headers=headers)
        jsonResponse = initialResponse.json()
        return jsonResponse['id']

    # Check transcription status
    def checkTranscriptionStatus(self,id):
        endpoint = "https://api.assemblyai.com/v2/transcript/%s"%(id)
        headers = {
            "authorization":  self.apikey,
        }
        response = requests.get(endpoint, headers=headers).json()
        print(response)
        return response['status']

    # Write to file if done
    def writeIfReady(self,id,fname):
        endpoint = "https://api.assemblyai.com/v2/transcript/%s"%(id)
        headers = {
            "authorization":  self.apikey,
        }
        response = requests.get(endpoint, headers=headers).json()
        if response['status'] == 'completed':
            self.writeToFile(response['text'],fname)

        return response['status']

    # Write transcription to a file
    def writeToFile(self,transcript,fname):
        if not os.path.exists('Transcriptions'):
            os.mkdir('Transcriptions')

        with open('Transcriptions/' + fname,'w') as f:
            f.writelines(transcript)