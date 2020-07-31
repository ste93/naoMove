import os
import winsound

import bcolors

from JsonEditor import jsonEditor
from NaoLibs.Common import sendToRobot
import Constants
from FileManagement import Archive


def readAndMove(filename, t):
    listAngles = jsonEditor.readDict(filename)
    # print (listAngles)
    sendToRobot.sendrobot(listAngles, t)


def reproduce(sequence):
    t = 0
    for x in sequence:
        # print Constants.list_of_moves[x]
        readAndMove(Constants.list_of_moves[x],t)
        t = 1
os.chdir("../")

# a = Archive.getRepertoire()["repertoire"][8]["choreo"]
# print (bcolors.OKMSG + a + bcolors.ENDC)
reproduce(['i', 'l', 'k', 'a', 'd', 'b', 'l', 'f', 'h', 'd', 'i', 'a', 'b', 'e', 'f', 'c'])
# reproduce(['f', 'k', 'i', 'g', 'm', 'h', 'l', 'j'])

# reproduce(['m', 'k', 'j', 'g', 'l', 'h', 'f', 'i'])
# reproduce(['c', 's', 'g', 'b', 'j', 'b', 's', 'r', 'e', 'q', 'r', 'm', 'n', 'n', 'q', 'b'])
# reproduce(['i', 'i', 'n', 'n', 'i', 'p', 'c', 'p', 'o', 'r', 'i', 'm', 'g', 's', 'k', 'j'] )
# reproduce(['j', 't', 's', 'p', 'o', 'l', 'c', 'c', 'o', 'c', 'f', 'h', 'n', 'n', 'o', 'r'])# 0.38756127451
# reproduce(['j', 'm', 'c', 'c', 'i', 'e', 'c', 'i']) #0.2
# reproduce(['b', 'f', 'a', 'l', 'c', 'h', 'm', 'd']) # 0.641944444444
# for x in Constants.repertoire.values():
#     print x
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)