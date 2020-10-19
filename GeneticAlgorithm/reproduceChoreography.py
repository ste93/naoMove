import json
import os
import sys
import winsound


from JsonEditor import jsonEditor
from NaoLibs.Common import sendToRobot, MoveForward, MoveBackward, Rotate


def readAndMove(filename, t):
    listAngles = jsonEditor.readDict(filename)
    sendToRobot.sendrobot(listAngles, t)


def reproduce(sequence):
    t = 1
    list_of_moves = jsonEditor.readDict_reproduce("./json/archive/list_of_moves")
    print list_of_moves
    sendToRobot.initialize()
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


os.chdir("../")
reproduce("awhzsnxpyabtxdjj")
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)