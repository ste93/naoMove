import json
import sys


def dumpDict(filename, dict):
    with open(filename+ '.json', 'w') as fp:
        json.dump(dict, fp)
    fp.close()

def readKinectDict(filename):
    with open("json/kinect/" + filename + '.json','r') as fp:
        file = json.load(fp)
        fp.close()
        return file

def readDict(filename):
    try:
        with open(filename+ '.json', 'r') as fp:
            file = json.load(fp)
            fp.close()
            return file
    except :
        print "Unexpected error: " + filename , sys.exc_info()[0]

