import math
import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb


class Curves_right():
    # Class defining curves A

    def __init__(self, R, Degree, Velocity, Range, ListPoint):
        t = 0.0
        while t <= Range:
            self.x = Velocity * t
            self.y = R * math.cos(t + Degree)
            self.z = R * math.sin(
                t + Degree
            ) - 0.0032 * Velocity * Velocity * t * t + 0.16 * Velocity * t

            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class Curves_left():
    # Class defining curves A

    def __init__(self,
                 R,
                 Degree,
                 Velocity,
                 Range,
                 ListPoint,
                 offsetY=0,
                 offsetZ=0):
        t = 0
        while t <= Range:
            self.x = Velocity * t
            self.y = R * math.sin(t + Degree) + offsetY
            self.z = R * math.cos(
                t + Degree
            ) - 0.0032 * Velocity * Velocity * t * t + 0.16 * Velocity * t + offsetZ
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class Line():
    def __init__(self, y, z, Range, ListPoint):
        t = 0.0
        while t <= Range:
            self.x = t * 1.0
            self.y = y * 1.0
            self.z = z - 0.0032 * t * t + 0.16 * t

            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 5


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list