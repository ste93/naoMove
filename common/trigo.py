import math

def distanceBetween2Points3D(x1, y1, z1,
                             x2, y2, z2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))


def distanceBetween2Points2D(x1, y1,
                             x2, y2):
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


def dot(x, y):
    """Dot product as sum of list comprehension doing element-wise multiplication"""
    return sum(x_i*y_i for x_i, y_i in zip(x, y))

def mag(x):
    return math.sqrt(sum(i**2 for i in x))


def angleBetween3Points2D( x1, y1,
                           x2, y2,
                           x3, y3):  # calulates the ElbowYaw value for the Right elbow by using geometry
    p12 = distanceBetween2Points2D(x1, y1, x2, y2)
    p13 = distanceBetween2Points2D(x1, y1, x3, y3)
    p23 = distanceBetween2Points2D(x2, y2, x3, y3)
    return math.acos((math.pow(p12, 2) + math.pow(p13, 2) - math.pow(p23, 2)) / (2 * p12 * p13))


def angleBetween3Points3D( x1, y1, z1,
                           x2, y2, z2,
                           x3, y3, z3):  # calulates the ElbowYaw value for the Right elbow by using geometry
    v1 = {"x": x1 - x2, "y": y1 - y2,"z": z1 - z2}
    v2 =  {"x": x3 - x2, "y": y3 - y2,"z":  z3 - z2}

    v1mag = math.sqrt(v1["x"] * v1["x"] + v1["y"]  * v1["y"]  + v1["z"]  * v1["z"] )
    v1norm = {"x": v1["x"] / v1mag, "y": v1["y"] / v1mag, "z": v1["z"] / v1mag}

    v2mag = math.sqrt(v2["x"] * v2["x"] + v2["y"] * v2["y"] + v2["z"] * v2["z"])
    v2norm = { "x":v2["x"] / v2mag, "y": v2["y"] / v2mag,  "z":v2["z"] / v2mag}
    res = v1norm["x"] * v2norm["x"] + v1norm["y"] * v2norm["y"] + v1norm["z"] * v2norm["z"]
    if res > 1:
        res = 1
    elif res < -1:
        res = -1
    angle = math.acos(res)
    angle = math.degrees(angle)
    return angle


def distanceOfPointFromLine(x1, y1, #punto 1 retta
                            x2, y2, #punto 2 retta
                            xP, yP): #punto da calcolare distanza
    m = float(y2 - y1)/(x2-x1)
    q = y1 - (m*x1)
    distanza = abs(yP - (m * xP + q)) / math.sqrt(1 + math.pow(m, 2))
    return distanza