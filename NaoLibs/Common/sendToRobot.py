import sys

import motion
from naoqi import ALProxy
from naoqi import ALModule
import almath
import constants
import config
import time
import qi





from Mathematical import trigo

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def sendrobot(anglelist,t):
    robotIP = constants.robotIP
    # robotIP = "127.0.0.1"
    PORT = constants.PORT
    # s = qi.Session()
    # s.connect("tcp://127.0.0.1:9559")

    # imagine you have a NAOqi proxy on almemory
    # mem = ALProxy("ALMemory", robotIP, PORT)
    # mem.getData("ALMotion/RobotIsFalling")
    # get a qi session
    # mem.subscribeToEvent("ALMotion/RobotIsStand", "MyModule", "myCallback")
    # mem.subscribeToEvent("ALMotion/RobotIsFalling", "MyModule", "myCallback")
    #
    # print mem.getSubscribers("ALMotion/RobotIsStand")
    # print mem.getMicroEventList()
    # print mem.getEventList()
    # robotIP = "192.168.1.10"  # raw_input("robot IP: ")
    # PORT = 9559  # int(raw_input("robot Port (standard 9559): "))
    try:
        try:
            motionProxy = ALProxy("ALMotion", robotIP, PORT) #creates proxy to call specific functions
        except Exception, e:
            print "Could not create proxy to AlMotion"
            print "Error was: ", e
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, PORT) #creates proxy to call specific functions
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        names = []
        angleLists = []
        timeLists = []
        for name in anglelist["angles"]:
            names.append(str(name))
            angleLists.append(float(anglelist["angles"][name])*almath.TO_RAD)
            timeLists.append(4)
        StiffnessOn(motionProxy)
        if (t == 0): # if it is the first time the robot is called upon
            motionProxy.setStiffnesses("Body", 0.0) # unstiffens the joints
            motionProxy.wbEnable(True)

            postureProxy.goToPosture("Stand", 10) # gets the robot into his initial standing position
            print("init")
            t = t+1
            # chainName = "Torso"
            # frame = motion.FRAME_ROBOT
            # position = [0.0, 0.05, 0.3, 0.1, 0.0, 0.0]  # Absolute Position
            # fractionMaxSpeed = 0.05
            # axisMask = 63
            # motionProxy.setPositions(chainName, frame, position, fractionMaxSpeed, axisMask)

        isAbsolute = True # kindoff is deprecated, but makes the joint positions absolute and not relative
        # print anglelist["supportLeg"]
        motionProxy.wbEnable(True)
        # motionProxy.wbFootState("Plane", str(anglelist["supportLeg"]))
        # isEnable = True
        # supportLeg = str(anglelist["supportLeg"])
        # motionProxy.wbEnableBalanceConstraint(isEnable, supportLeg)
        # legName = ["LLeg", "RLeg"]
        # X = 0.06
        # Y = 0.1
        # Theta = 0.0
        # footSteps = [[X, Y, Theta], [X, -Y, Theta]]
        # timeList = [0.6, 1.2]
        # clearExisting = False
        # motionProxy.setFootSteps(legName, footSteps, timeList, clearExisting)

        # X = 0.8
        # Y = 0.0
        # Theta = 0.0
        # Frequency = 0.0  # max speed
        # motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

        motionProxy.angleInterpolation(names, angleLists, timeLists, True) #the function talks with the robot
        motionProxy.setCollisionProtectionEnabled("Arms", True)
        # ankle_position = motionProxy.getPosition("RAnklePitch", motion.FRAME_TORSO, True)
        # z0 = trigo.distanceBetween2Points3D(com_position[0], com_position[1], com_position[2],
        #                                     ankle_position[0], ankle_position[1], ankle_position[2])
        # print z0
        # t += 1 # global t gets added by 1 so the joints dont get unstiffened again and the robot does not get put in its initial position
    except Exception as e: # checks for any and all errors
        print "error in here " , e
         # ignores every single one of them, except keyboardInterupt and SystemExit
    except (KeyboardInterrupt, SystemExit): # when the program gets terminated
        print("error program terminated")
        postureProxy.goToPosture("StandInit", 0.5) # set the robot in its initial position
        motionProxy.setStiffnesses("Body", 1.0) # stiffen the joints
        raise #actually quit
