from lib2 import angles2 as angles
import os
from common import jsonEditor
from common import sendToRobotMultipleMovements as sendToRobot

filename = 'garage21022020'
dirName = "json/2/" + filename
data = jsonEditor.readKinectDict(filename)
t = 0
if not os.path.exists(dirName):
    os.mkdir(dirName)

for key in data['datafile']:
    value = key['data']
    listAngles = angles.anglesList(value)
    jsonEditor.dumpDict(dirName + "/" + str(t), listAngles)
    listAngles = jsonEditor.readDict(dirName + "/" + str(t))
    print (listAngles)
    sendToRobot.sendrobot(listAngles,t)
    t = t + 1
