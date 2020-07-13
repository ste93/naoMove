import time

import bcolors as bcolors

# import angles
from JsonEditor import jsonEditor
from NaoLibs.Common import sendToRobot

def readAndMove(filename, t):
    listAngles = jsonEditor.readDict(filename)
    print (listAngles)
    # here can be added the balance
    sendToRobot.sendrobot(listAngles, t)


filenames = [
        "json/finiti/arms45",
        "json/finiti/armsdown",
        "json/finiti/armsforward",
        "json/finiti/sadleft",
        "json/finiti/armsinit",
        "json/finiti/extremelysad",
        "json/finiti/openarms",
        "json/finiti/openarmsextended",
        "json/finiti/request",
        "json/finiti/swordleft",
        "json/finiti/swordright",
        "json/finiti/sadright",
        "json/finiti/extremelysadchest",
        "json/finiti/rightup45",
        "json/finiti/rightopen",
        "json/finiti/swordrightleftrequest",
        "json/finiti/rightsadchest",
        "json/finiti/requestright"

             ]


t = 0
for file in filenames:
    print(bcolors.OKMSG + file + bcolors.ENDC)
    readAndMove(file, t)
    t = 1


time.sleep(2)
