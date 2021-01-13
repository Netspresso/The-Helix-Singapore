import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
from config import Curve as C
from curves import linspace, Curves_right, Line, Curves_left
# import numpy as np

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()
'''Here I began script'''
''' Classes '''

# Lists of points for all Curves
ptList = []
n_of_curve = 10
# count of curves

# Loop which adds empty lists to ptList (now we have list which contain 18 empty lists)
for i in range(0, n_of_curve):
    ptList.append([])

# Generating points
Curves_right(2.5, C.fi1, C.v, C.Range, ptList[0])
Curves_left(2.5, C.fi1, C.v, C.Range, ptList[1])
Curves_right(2.5, C.fi2, C.v, C.Range, ptList[2])
Curves_left(2.5, C.fi2, C.v, C.Range, ptList[3])
Curves_right(2.5, C.fi3, C.v, C.Range, ptList[4])
Curves_left(2.5, C.fi3, C.v, C.Range, ptList[5])
Curves_right(2.5, C.fi4, C.v, C.Range, ptList[6])
Curves_left(2.5, C.fi4, C.v, C.Range, ptList[7])
# Line(math.sqrt(3), 0, -20, 8, ptList[4])
# Line(math.sqrt(3) - 1, 0, -20, 8, ptList[5])
# Line(-math.sqrt(3) + 1, 0, 12, 40, ptList[6])
# Line(-math.sqrt(3), 0, 12, 40, ptList[7])
# Line(math.sqrt(3), 1.5, -20, 8, ptList[8])
# Line(math.sqrt(3) - 1, 1.5, -20, 8, ptList[9])
# Line(-math.sqrt(3) + 1, 1.5, 12, 40, ptList[10])
# Line(-math.sqrt(3), 1.5, 12, 40, ptList[11])
Line(-C.length, -C.length, 50, ptList[8])
Line(C.length, -C.length, 50, ptList[9])

#  Creating curves through the points
length = len(ptList)
for Curve in range(0, length):
    controlPoints = ptList[Curve]  # Lista punktów kontrolnych
    n = len(controlPoints)
    deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
    m = n + deg + 1
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

beam_ptList = []
n_of_beams = len(ptList[8])
for i in range(0, n_of_beams):
    beam_ptList.append([])

for i in range(0, n_of_beams):
    beam_ptList[i].append(ptList[8][i])
    beam_ptList[i].append(ptList[9][i])

for beam in range(0, len(beam_ptList)):
    for point in beam_ptList[beam]:
        controlPoints = beam_ptList[beam]  # Lista punktów kontrolnych
        n = len(controlPoints)
        deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
        m = n + deg + 1
        knotPoints = linspace(0, 1, m)
        createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

length = len(ptList[0])
# Prawoskret
for j in range(0, 6, 2):
    for i in range(0, length, 4):
        controlPoints = [ptList[j][i], ptList[j + 2][i]]
        n = len(controlPoints)
        deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
        m = n + deg + 1
        knotPoints = linspace(0, 1, m)
        createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

# Krzywa 6 i 0
for i in range(0, length, 4):
    controlPoints = [ptList[0][i], ptList[6][i]]
    n = len(controlPoints)
    deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
    m = n + deg + 1
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

# lewoskret
for j in range(1, 7, 2):
    for i in range(0, length, 4):
        controlPoints = [ptList[j][i], ptList[j + 2][i]]
        n = len(controlPoints)
        deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
        m = n + deg + 1
        knotPoints = linspace(0, 1, m)
        createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

# Krzywa 7 i 1
for i in range(0, length, 4):
    controlPoints = [ptList[1][i], ptList[7][i]]
    n = len(controlPoints)
    deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
    m = n + deg + 1
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()