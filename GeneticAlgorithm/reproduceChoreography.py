import json
import os
import sys
import winsound


from JsonEditor import jsonEditor
from NaoLibs.Common import sendToRobot, MoveForward, MoveBackward, Rotate


def readAndMove(filename, t):
    listAngles = jsonEditor.readDict(filename)
    # print (listAngles)
    sendToRobot.sendrobot(listAngles, t)


def reproduce(sequence):
    t = 0
    list_of_moves = jsonEditor.readDict_reproduce("./json/archive/list_of_moves")
    print list_of_moves
    for pose in sequence:
        # print Constants.list_of_moves[x]
        if pose == "z":
            MoveForward.move_forward(t)
        elif pose == "y": # z and y are the walk and the rotation
            MoveBackward.move_backward(t)
        elif pose =="x":
            Rotate.rotate_left(t)
        elif pose == "w":
            Rotate.rotate_right(t)
        else:
            readAndMove(list_of_moves[pose],t)
        t = 1


os.chdir("../")
# a = Archive.getRepertoire()["repertoire"][8]["choreo"]
# print (bcolors.OKMSG + a + bcolors.ENDC)
# reproduce("abebmlfiabbcadke")
reproduce("abcewhvxfnubzrha")
# reproduce(['f', 'k', 'i', 'g', 'm', 'h', 'l', 'j'])
# aznwrytxmagxzwty
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