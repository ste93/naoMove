import json

def dumpDict(filename, dict):
    with open(filename+ '.json', 'w') as fp:
        json.dump(dict, fp)

def readKinectDict(filename):
    with open("json/kinect/" + filename + '.json','r') as fp:
        return json.load(fp)

def readDict(filename):
    with open(filename+ '.json', 'r') as fp:
        return json.load(fp)