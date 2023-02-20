'''
Write transcripts to file if they're ready
'''
'''
Script for checking transcription status by file
'''
import sys
import os
from Transcriber import Transcriber

def writeIfReady(fname,basename):
    t = Transcriber(os.environ['AAI_API_KEY'])
    with open(fname,'r') as f:
        lines = f.readlines()

    c = 0
    for line in lines:
        fname = '%s_%d.txt'%(basename,c)
        try:
            # If we already wrote it, skip it
            if os.path.exists('Transcriptions/%s'%fname):
                print('Transcriptions/%s exists'%fname)
                c +=1
                continue

            print("Writing %s"%fname)
            t.writeIfReady(line,fname)
            print("Success! \n ------------------- \n")
        except:
            print("Error on id %s file %s"%(line,fname))
        c+=1
if __name__ == "__main__":
    fname = sys.argv[1]
    basename = sys.argv[2]
    writeIfReady(fname,basename)