import json
import sys
import os


def dumpDict(filename, dict):
    with open(filename+ '.json', 'w') as fp:
        json.dump(dict, fp)
    fp.close()


def readKinectDict(filename):
    with open("json/kinect/" + filename + '.json','r') as fp:
        file_opened = json.load(fp)
        fp.close()
        return file_opened


def readDict(filename):
    try:
        with open(filename+ '.json', 'r') as fp:
            file_opened = json.load(fp)
            fp.close()
            return file_opened
    except Exception as e :
        print "Unexpected error: " + filename , sys.exc_info()[0]
        print e



def readDict_reproduce(filename):
    # print "workingdir ",  os.getcwd()
    # root = filename
    # for path, subdirs, files in os.walk(root):
    #     for name in files:
    #         if "moves" in name:
    #             print os.path.join(path, name)
    #         print filename+ '.json'
    try:
        with open(filename+ '.json', 'r') as fp:
            file_opened = json.load(fp)
            fp.close()
            return file_opened
    except Exception as e :
        print "Unexpected error: " + filename , sys.exc_info()[0]
        print e
