'''
Script to check transcription process
'''
import sys
import os
import requests

def checkStatus(id):
    endpoint = "https://api.assemblyai.com/v2/transcript/%s"%(id)
    headers = {
        "authorization":  os.environ['AAI_API_KEY'],
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def parseResults(response):
    transcript = response['text']
    print(transcript)

if __name__ == "__main__":
    id = sys.argv[1]
    response = checkStatus(id)
    if response['status'] == 'completed':
        parseResults(response)
    else:
        print(response)
        