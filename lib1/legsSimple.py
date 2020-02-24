import math
from common import trigo


def calculateKneePitch(x1, y1, z1, #1 is the hip position
                       x2, y2, z2, #2 is the knee position
                       x3, y3, z3): #3 is the ankle position
    angle = 180 - trigo.angleBetween3Points3D(x1, y1, z1,
                                              x2, y2, z2,
                                              x3, y3, z3)
    if angle > 121:
        angle = 121
    elif angle < -5:
        angle = -5
    return angle

def calculateAnklePitch(x1, y1, z1,  # 1 is the hip position
                        x2, y2, z2,  # 2 is the knee position
                        x3, y3, z3):  # 3 is the ankle position
    # angle = 90 - trigo.angleBetween3Points3D(x1, y1, z1,
    # x2, y2, z2,
    # x3, y3, z3)
    # print("ankle " + str(angle))
    # if angle > 52:
    #     angle = 52
    # elif angle < -68:
    #     angle = -68
    # return angle
    if (y2 < y1):
        angle = math.atan(abs(y2 - y1) / abs(z2 - z1))
        angle = -90 + math.degrees(angle)
        print("ankle if " + str(angle))
        if (angle < -68):
            angle = -68
        return angle
    else:
        angle = math.atan((z2 - z1) / (y2 - y1))
        angle = math.degrees(angle)
        angle = -90 - angle
        print("ankle else " + str(angle))
        if angle > 52:
            angle = 52
        return angle

#def ca


def calculateHipPitchYaw(x1, y1, z1, #1 is the shoulder center position
                         x2, y2, z2, #2 is the spine position
                         x3, y3, z3): #3 is the hip center position
    v1 = [x1, y1, z1]
    v2 = [x2, y2, z2]
    v3 = [x3, y3, z3]
    spine = [x1 - x2, y1 - y2, z1 - z2]
    pelvis = [x3-x2, y3-y2, z3-z2]
    res1 = trigo.dot(spine, pelvis)
    mags = trigo.mag(spine) * trigo.mag(pelvis)



def calculateHipPitch(x1, y1, z1,  # 1 is the hip position
                        x2, y2, z2):  # 2 is the knee position
    if (y2 < y1):
        angle = math.atan(abs(y2 - y1) / abs(z2 - z1))
        angle = -90 + math.degrees(angle)
        print("hipPitch if " + str(angle))
        if (angle < -88):
            angle = -88
        return angle
    else:
        angle = math.atan((z2 - z1) / (y2 - y1))
        angle = math.degrees(angle)
        angle = -90 - angle
        print("hipPitch else " + str(angle))
        if angle > 27:
            angle = 27
        return angle

def calculateHipRoll(x1, y1, z1,  # 1 is the hip position
                     x2, y2, z2, left):  # 2 is the knee position
    if(z2<z1):
        test = z2
        z2 = z1
        z1 = test
    if (z2 - z1 < 0.1):
        z2 = 1.0
        z1 = 0.8
    angle = math.atan((x2 - x1) / (z2 - z1))
    print left
    print "hip roll " + str(angle)
    if not left:
        angle = - math.degrees(angle)
    return angle
