import json
import time
from lib1 import angles
# import angles
from common import jsonEditor, sendToRobot
def readAndMove(filename):
    listAngles = jsonEditor.readDict(filename)
    print (listAngles)
    sendToRobot.sendrobot(listAngles, 0)


# filenames = ["json/1/garage4/3",
#              "json/1/garage4/4",
#              "json/1/garage4/5",
#              "json/1/garage4/7",
#              "json/1/garage4/10",
#              "json/1/garage4/11",
#              "json/1/garage4/13",
#              "json/1/ppp/21"]

filenames = ["json/finiti/sxAlzata",
             "json/finiti/sxdietro",
             "json/finiti/dxAlzata"
             # "json/finiti/dxdietro"
             ]

for file in filenames:
    readAndMove(file)


time.sleep(2)
