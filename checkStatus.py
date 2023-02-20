'''
Script for checking transcription status by file
'''
import sys
import os
from Transcriber import Transcriber

def checkStatus(fname):
    t = Transcriber(os.environ['AAI_API_KEY'])
    with open(fname,'r') as f:
        lines = f.readlines()
    
    cc = 0
    for line in lines:
        status = t.checkTranscriptionStatus(line)
        if status == 'completed':
            cc +=1
    
    n = len(lines)
    percDone = 100.0 * cc / n
    print("Transcription %0.2f percent completed"%percDone)

if __name__ == "__main__":
    fname = sys.argv[1]
    checkStatus(fname)