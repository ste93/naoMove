import math

def angleRShoulderPitch(x2, y2, z2, x1, y1, z1): #calulates the Shoulderpitch value for the Right shoulder by using geometry
    if(y2<y1):
        angle = math.atan(abs(y2 - y1) / abs(z2 - z1))
        angle = math.degrees(angle)
        angle = -(angle)
        if(angle<-118):
            angle = -117
        return angle
    else:
        angle = math.atan((z2-z1)/(y2-y1))
        angle = math.degrees(angle)
        angle = 90-angle
        return angle

def angleRShoulderRoll(x2, y2, z2, x1, y1, z1): #calulates the ShoulderRoll value for the Right shoulder by using geometry
    if(z2<z1):
        test = z2
        anderetest = z1
        z2=anderetest
        z1=test
    if (z2 - z1 < 0.1):
        z2 = 1.0
        z1 = 0.8
    angle = math.atan((x2 - x1) / (z2 - z1))
    angle = math.degrees(angle)
    return angle

def angleLShoulderPitch(x2, y2, z2, x1, y1, z1): #calulates the Shoulderpitch value for the Left shoulder by using geometry
    if (y2 < y1):
        angle = math.atan(abs(y2 - y1) / abs(z2 - z1))
        angle = math.degrees(angle)
        angle = -(angle)
        if (angle < -118):
            angle = -117
        return angle
    else:
        angle = math.atan((z2 - z1) / (y2 - y1))
        angle = math.degrees(angle)
        angle = 90 - angle
        return angle

def angleLShouderRoll(x2, y2, z2, x1, y1, z1): #calulates the ShoulderRoll value for the Left shoulder by using geometry
    if (z2 < z1):
        test = z2
        anderetest = z1
        z2 = anderetest
        z1 = test
    if(z2-z1< 0.1):
        z2=1.0
        z1=0.8
    angle = math.atan((x2-x1)/(z2-z1))
    angle = math.degrees(angle)
    return angle


def angleRElbowYaw(x2, y2, z2, x1, y1, z1,shoulderpitch): #calulates the ElbowYaw value for the Right elbow by using geometry
    if abs(y2 - y1)<0.2 and abs(z2 - z1) < 0.2 and (x1 < x2):
        return 0
    elif(abs(x2-x1)<0.1 and abs(z2-z1)<0.1 and (y1>y2)):
        return 90
    elif(abs(x2-x1)<0.1 and abs(z2-z1)<0.1 and (shoulderpitch > 50)):
        return 90
    elif(abs(y2-y1)<0.1 and abs(z2-z1)<0.1 and (shoulderpitch < 50)):
        return 0
    elif(abs(x2-x1)<0.1 and abs(y2-y1)<0.1 and (shoulderpitch > 50)):
        return 90
    else:
        angle = math.atan((z2 - z1) / (y2 - y1))
        angle = math.degrees(angle)
        angle = - angle + (shoulderpitch)
        angle = - angle
        return angle


def angleRElbowRoll(x3, y3, z3, x2, y2, z2, x1, y1, z1): #calulates the ElbowRoll value for the Right elbow by using geometry
    a1=(x3-x2)**2+(y3-y2)**2 + (z3-z2)**2
    lineA= a1 ** 0.5                        # calculates length of line between 2 3D coordinates
    b1=(x2-x1)**2+(y2-y1)**2 + (z2-z1)**2
    lineB= b1 ** 0.5                        # calculates length of line between 2 3D coordinates
    c1=(x1-x3)**2+(y1-y3)**2 + (z1-z3)**2
    lineC= c1 ** 0.5                        # calculates length of line between 2 3D coordinates

    cosB = (pow(lineA, 2) + pow(lineB,2) - pow(lineC,2))/(2*lineA*lineB)
    acosB = math.acos(cosB)
    angle = math.degrees(acosB)
    angle = 180 - angle
    return angle


def angleLElbowYaw(x2, y2, z2, x1, y1, z1, shoulderpitch): #calulates the ElbowYaw value for the Left elbow by using geometry
    if(abs(y2-y1)<0.2 and abs(z2-z1) < 0.2 and (x1>x2) ):
        return 0
    elif(abs(x2-x1)<0.1 and abs(z2-z1)<0.1 and (y1>y2)):
        return -90
    elif(abs(x2-x1)<0.1 and abs(z2-z1)<0.1 and (shoulderpitch > 50)):
        return -90
    elif(abs(y2-y1)<0.1 and abs(z2-z1)<0.1 and (shoulderpitch > 50)):
        return 0
    elif(abs(x2-x1)<0.1 and abs(y2-y1)<0.1 and (shoulderpitch > 50)):
        return -90
    else:
        angle = math.atan((z2 - z1) / (y2 - y1))
        angle = math.degrees(angle)
        angle = - angle + (shoulderpitch)
        angle = - angle
        return angle

def angleLElbowRoll(x3, y3, z3, x2, y2, z2, x1, y1, z1): #calulates the ElbowRoll value for the Left elbow by using geometry

    a1=(x3-x2)**2+(y3-y2)**2 + (z3-z2)**2
    lineA= a1 ** 0.5                        # calculates length of line between 2 3D coordinates
    b1=(x2-x1)**2+(y2-y1)**2 + (z2-z1)**2
    lineB= b1 ** 0.5                        # calculates length of line between 2 3D coordinates
    c1=(x1-x3)**2+(y1-y3)**2 + (z1-z3)**2
    lineC= c1 ** 0.5                        # calculates length of line between 2 3D coordinates

    cosB = (pow(lineA, 2) + pow(lineB,2) - pow(lineC,2))/(2*lineA*lineB)
    acosB = math.acos(cosB)
    angle = math.degrees(acosB)
    angle = -180+ angle
    return angle
