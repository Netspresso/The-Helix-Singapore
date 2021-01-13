# coding: utf-8
# Macro created by MSC Apex 2020 PRE - Version CLR:722475
# Macro created on Nov 18, 2020 at 11:38:10
#
# Macro Name = beleczki
#
# Macro Description =
#
# Macro Hot Key =
#
# Initialize environment for macro execution
#

import apex
from apex.construct import Point3D, Point2D

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()

#
# Start of recorded operations
#

result = apex.session.display2DSpans(False)

result = apex.session.display3DSpans(True)

beamshape_1 = apex.attribute.createBeamShapeHollowRoundByThickness(
    name="Beam Shape", outerRadius=0.1, thickness=0.01)

result = apex.session.display2DSpans(False)

result = apex.session.display3DSpans(True)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125411'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
_ids = '125412'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125413'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125414'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125415'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125416'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125417'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

pathEdges_ = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 7")
_ids = '125418'
pathEdges_.extend(curve_1.getEdges(ids=_ids))
beamTarget_ = apex.geometry.EdgeCollection()
for entity in pathEdges_:
    beamTarget_.append(entity.asEdge())
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeA_ = beamShape_
beamShape_ = apex.catalog.getBeamShape('Beam Shape 2')
shapeB_ = beamShape_
beamspans = apex.attribute.createBeamSpanFree(
    name="Span",
    beamTarget=beamTarget_,
    shapeEndA=shapeA_,
    shapeEndB=shapeB_,
    shapeEndA_orientation=0.0,
    shapeEndB_orientation=0.0,
    shapeEndA_offset1=0.0,
    shapeEndA_offset2=0.0,
    shapeEndB_offset1=0.0,
    shapeEndB_offset2=0.0,
)

# for i in range(22, 39):
#     _target = apex.EntityCollection()
#     part_1 = apex.getPart(pathName="gen/Part 1")
#     curve_1 = part_1.getCurve(name="Curve {}".format(i))
#     _target.extend(curve_1.getEdges())
#     result = apex.geometry.fillerSurface(target=_target)