import bcolors

from NaoLibs.lib1 import angles_2 as angles
import os
from JsonEditor import jsonEditor
from NaoLibs.Common import sendToRobot
from Mathematical import plot3d

# filename = 'prova8maggio'
filename = 'provanoh1'
# filename = 'nohbasics'
dirName = "json/1/" + filename
data = jsonEditor.readKinectDict(filename)
t = 0
if not os.path.exists(dirName):
    os.mkdir(dirName)

for key in data['datafile']:
    value = key['data']
    print bcolors.ERRMSG + "number",key["coord"] + bcolors.ENDC
    listAngles = angles.anglesList(value)
    jsonEditor.dumpDict(dirName + "/" + str(t), listAngles)
    listAngles = jsonEditor.readDict(dirName + "/" + str(t))
    sendToRobot.sendrobot(listAngles,t)
    # plot3d.printplot(key)
    t = t + 1
