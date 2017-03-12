# ./schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-03-12 19:15:18.808875 by PyXB version 1.2.5 using Python 3.6.0.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d94a796e-074f-11e7-bca3-7054d2191245')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: distance
class distance (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'distance')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 4, 4)
    _Documentation = None
distance._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.float, value=pyxb.binding.datatypes._fp(0.0))
distance._InitializeFacetMap(distance._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'distance', distance)
_module_typeBindings.distance = distance

# Atomic simple type: obstacleRole
class obstacleRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obstacleRole')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 153, 4)
    _Documentation = None
obstacleRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=obstacleRole, enum_prefix=None)
obstacleRole.static = obstacleRole._CF_enumeration.addEnumeration(unicode_value='static', tag='static')
obstacleRole.dynamic = obstacleRole._CF_enumeration.addEnumeration(unicode_value='dynamic', tag='dynamic')
obstacleRole._InitializeFacetMap(obstacleRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'obstacleRole', obstacleRole)
_module_typeBindings.obstacleRole = obstacleRole

# Atomic simple type: obstacleType
class obstacleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obstacleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 160, 4)
    _Documentation = None
obstacleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=obstacleType, enum_prefix=None)
obstacleType.unknown = obstacleType._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
obstacleType.parkedVehicle = obstacleType._CF_enumeration.addEnumeration(unicode_value='parkedVehicle', tag='parkedVehicle')
obstacleType.constructionZone = obstacleType._CF_enumeration.addEnumeration(unicode_value='constructionZone', tag='constructionZone')
obstacleType.roadBoundary = obstacleType._CF_enumeration.addEnumeration(unicode_value='roadBoundary', tag='roadBoundary')
obstacleType.car = obstacleType._CF_enumeration.addEnumeration(unicode_value='car', tag='car')
obstacleType.truck = obstacleType._CF_enumeration.addEnumeration(unicode_value='truck', tag='truck')
obstacleType.bus = obstacleType._CF_enumeration.addEnumeration(unicode_value='bus', tag='bus')
obstacleType.bicycle = obstacleType._CF_enumeration.addEnumeration(unicode_value='bicycle', tag='bicycle')
obstacleType.pedestrian = obstacleType._CF_enumeration.addEnumeration(unicode_value='pedestrian', tag='pedestrian')
obstacleType.priorityVehicle = obstacleType._CF_enumeration.addEnumeration(unicode_value='priorityVehicle', tag='priorityVehicle')
obstacleType._InitializeFacetMap(obstacleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'obstacleType', obstacleType)
_module_typeBindings.obstacleType = obstacleType

# Atomic simple type: lineMarking
class lineMarking (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineMarking')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 204, 4)
    _Documentation = None
lineMarking._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineMarking, enum_prefix=None)
lineMarking.dashed = lineMarking._CF_enumeration.addEnumeration(unicode_value='dashed', tag='dashed')
lineMarking.solid = lineMarking._CF_enumeration.addEnumeration(unicode_value='solid', tag='solid')
lineMarking._InitializeFacetMap(lineMarking._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lineMarking', lineMarking)
_module_typeBindings.lineMarking = lineMarking

# Atomic simple type: drivingDir
class drivingDir (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'drivingDir')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 231, 4)
    _Documentation = None
drivingDir._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=drivingDir, enum_prefix=None)
drivingDir.same = drivingDir._CF_enumeration.addEnumeration(unicode_value='same', tag='same')
drivingDir.opposite = drivingDir._CF_enumeration.addEnumeration(unicode_value='opposite', tag='opposite')
drivingDir._InitializeFacetMap(drivingDir._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'drivingDir', drivingDir)
_module_typeBindings.drivingDir = drivingDir

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 287, 12)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.n1_0 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='1.0', tag='n1_0')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Complex type floatInterval with content type ELEMENT_ONLY
class floatInterval (pyxb.binding.basis.complexTypeDefinition):
    """Complex type floatInterval with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatInterval')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 19, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element exact uses Python identifier exact
    __exact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'exact'), 'exact', '__AbsentNamespace0_floatInterval_exact', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 21, 12), )

    
    exact = property(__exact.value, __exact.set, None, None)

    
    # Element intervalStart uses Python identifier intervalStart
    __intervalStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'intervalStart'), 'intervalStart', '__AbsentNamespace0_floatInterval_intervalStart', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 23, 16), )

    
    intervalStart = property(__intervalStart.value, __intervalStart.set, None, None)

    
    # Element intervalEnd uses Python identifier intervalEnd
    __intervalEnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'intervalEnd'), 'intervalEnd', '__AbsentNamespace0_floatInterval_intervalEnd', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 24, 16), )

    
    intervalEnd = property(__intervalEnd.value, __intervalEnd.set, None, None)

    _ElementMap.update({
        __exact.name() : __exact,
        __intervalStart.name() : __intervalStart,
        __intervalEnd.name() : __intervalEnd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.floatInterval = floatInterval
Namespace.addCategoryObject('typeBinding', 'floatInterval', floatInterval)


# Complex type point with content type ELEMENT_ONLY
class point (pyxb.binding.basis.complexTypeDefinition):
    """Complex type point with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'point')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 36, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_point_x', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 38, 12), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_point_y', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 39, 12), )

    
    y = property(__y.value, __y.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.point = point
Namespace.addCategoryObject('typeBinding', 'point', point)


# Complex type rectangle with content type ELEMENT_ONLY
class rectangle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type rectangle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rectangle')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 55, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_rectangle_length', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 57, 12), )

    
    length = property(__length.value, __length.set, None, None)

    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_rectangle_width', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 58, 12), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_rectangle_orientation', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 59, 12), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element centerPoint uses Python identifier centerPoint
    __centerPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'centerPoint'), 'centerPoint', '__AbsentNamespace0_rectangle_centerPoint', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 60, 12), )

    
    centerPoint = property(__centerPoint.value, __centerPoint.set, None, None)

    _ElementMap.update({
        __length.name() : __length,
        __width.name() : __width,
        __orientation.name() : __orientation,
        __centerPoint.name() : __centerPoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.rectangle = rectangle
Namespace.addCategoryObject('typeBinding', 'rectangle', rectangle)


# Complex type circle with content type ELEMENT_ONLY
class circle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type circle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'circle')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 74, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_circle_radius', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 76, 12), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element centerPoint uses Python identifier centerPoint
    __centerPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'centerPoint'), 'centerPoint', '__AbsentNamespace0_circle_centerPoint', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 77, 12), )

    
    centerPoint = property(__centerPoint.value, __centerPoint.set, None, None)

    _ElementMap.update({
        __radius.name() : __radius,
        __centerPoint.name() : __centerPoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.circle = circle
Namespace.addCategoryObject('typeBinding', 'circle', circle)


# Complex type polygon with content type ELEMENT_ONLY
class polygon (pyxb.binding.basis.complexTypeDefinition):
    """Complex type polygon with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'polygon')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 99, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_polygon_point', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 101, 12), )

    
    point = property(__point.value, __point.set, None, None)

    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.polygon = polygon
Namespace.addCategoryObject('typeBinding', 'polygon', polygon)


# Complex type shape with content type ELEMENT_ONLY
class shape (pyxb.binding.basis.complexTypeDefinition):
    """Complex type shape with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shape')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 117, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element rectangle uses Python identifier rectangle
    __rectangle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rectangle'), 'rectangle', '__AbsentNamespace0_shape_rectangle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 119, 12), )

    
    rectangle = property(__rectangle.value, __rectangle.set, None, None)

    
    # Element circle uses Python identifier circle
    __circle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'circle'), 'circle', '__AbsentNamespace0_shape_circle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 120, 12), )

    
    circle = property(__circle.value, __circle.set, None, None)

    
    # Element polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'polygon'), 'polygon', '__AbsentNamespace0_shape_polygon', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 121, 12), )

    
    polygon = property(__polygon.value, __polygon.set, None, None)

    _ElementMap.update({
        __rectangle.name() : __rectangle,
        __circle.name() : __circle,
        __polygon.name() : __polygon
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.shape = shape
Namespace.addCategoryObject('typeBinding', 'shape', shape)


# Complex type occupancy with content type ELEMENT_ONLY
class occupancy (pyxb.binding.basis.complexTypeDefinition):
    """Complex type occupancy with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'occupancy')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 125, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_occupancy_shape', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 127, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__AbsentNamespace0_occupancy_time', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 128, 12), )

    
    time = property(__time.value, __time.set, None, None)

    _ElementMap.update({
        __shape.name() : __shape,
        __time.name() : __time
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.occupancy = occupancy
Namespace.addCategoryObject('typeBinding', 'occupancy', occupancy)


# Complex type state with content type ELEMENT_ONLY
class state (pyxb.binding.basis.complexTypeDefinition):
    """Complex type state with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'state')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 132, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__AbsentNamespace0_state_position', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 134, 12), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_state_orientation', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 146, 12), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__AbsentNamespace0_state_time', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 147, 12), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__AbsentNamespace0_state_velocity', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 148, 12), )

    
    velocity = property(__velocity.value, __velocity.set, None, None)

    
    # Element acceleration uses Python identifier acceleration
    __acceleration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'acceleration'), 'acceleration', '__AbsentNamespace0_state_acceleration', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 149, 12), )

    
    acceleration = property(__acceleration.value, __acceleration.set, None, None)

    _ElementMap.update({
        __position.name() : __position,
        __orientation.name() : __orientation,
        __time.name() : __time,
        __velocity.name() : __velocity,
        __acceleration.name() : __acceleration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.state = state
Namespace.addCategoryObject('typeBinding', 'state', state)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 135, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_CTD_ANON_point', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 137, 24), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element rectangle uses Python identifier rectangle
    __rectangle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rectangle'), 'rectangle', '__AbsentNamespace0_CTD_ANON_rectangle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 139, 28), )

    
    rectangle = property(__rectangle.value, __rectangle.set, None, None)

    
    # Element circle uses Python identifier circle
    __circle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'circle'), 'circle', '__AbsentNamespace0_CTD_ANON_circle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 140, 28), )

    
    circle = property(__circle.value, __circle.set, None, None)

    
    # Element polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'polygon'), 'polygon', '__AbsentNamespace0_CTD_ANON_polygon', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 141, 28), )

    
    polygon = property(__polygon.value, __polygon.set, None, None)

    _ElementMap.update({
        __point.name() : __point,
        __rectangle.name() : __rectangle,
        __circle.name() : __circle,
        __polygon.name() : __polygon
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type obstacle with content type ELEMENT_ONLY
class obstacle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type obstacle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'obstacle')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_obstacle_role', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 179, 12), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_obstacle_type', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 180, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_obstacle_shape', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 181, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Element trajectory uses Python identifier trajectory
    __trajectory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trajectory'), 'trajectory', '__AbsentNamespace0_obstacle_trajectory', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 183, 16), )

    
    trajectory = property(__trajectory.value, __trajectory.set, None, None)

    
    # Element occupancySet uses Python identifier occupancySet
    __occupancySet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'occupancySet'), 'occupancySet', '__AbsentNamespace0_obstacle_occupancySet', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 191, 16), )

    
    occupancySet = property(__occupancySet.value, __occupancySet.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_obstacle_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 201, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 201, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __role.name() : __role,
        __type.name() : __type,
        __shape.name() : __shape,
        __trajectory.name() : __trajectory,
        __occupancySet.name() : __occupancySet
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.obstacle = obstacle
Namespace.addCategoryObject('typeBinding', 'obstacle', obstacle)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 184, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_CTD_ANON__state', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 186, 28), )

    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        __state.name() : __state
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 192, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element occupancy uses Python identifier occupancy
    __occupancy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'occupancy'), 'occupancy', '__AbsentNamespace0_CTD_ANON_2_occupancy', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 194, 28), )

    
    occupancy = property(__occupancy.value, __occupancy.set, None, None)

    _ElementMap.update({
        __occupancy.name() : __occupancy
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type boundary with content type ELEMENT_ONLY
class boundary (pyxb.binding.basis.complexTypeDefinition):
    """Complex type boundary with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundary')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 211, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_boundary_point', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 213, 12), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element lineMarking uses Python identifier lineMarking
    __lineMarking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lineMarking'), 'lineMarking', '__AbsentNamespace0_boundary_lineMarking', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 215, 12), )

    
    lineMarking = property(__lineMarking.value, __lineMarking.set, None, None)

    _ElementMap.update({
        __point.name() : __point,
        __lineMarking.name() : __lineMarking
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.boundary = boundary
Namespace.addCategoryObject('typeBinding', 'boundary', boundary)


# Complex type laneletRefList with content type ELEMENT_ONLY
class laneletRefList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type laneletRefList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'laneletRefList')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 220, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lanelet uses Python identifier lanelet
    __lanelet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanelet'), 'lanelet', '__AbsentNamespace0_laneletRefList_lanelet', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 222, 12), )

    
    lanelet = property(__lanelet.value, __lanelet.set, None, None)

    _ElementMap.update({
        __lanelet.name() : __lanelet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.laneletRefList = laneletRefList
Namespace.addCategoryObject('typeBinding', 'laneletRefList', laneletRefList)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 223, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_3_ref', pyxb.binding.datatypes.integer, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 224, 20)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 224, 20)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type lanelet with content type ELEMENT_ONLY
class lanelet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type lanelet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lanelet')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 244, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element leftBoundary uses Python identifier leftBoundary
    __leftBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'leftBoundary'), 'leftBoundary', '__AbsentNamespace0_lanelet_leftBoundary', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 246, 12), )

    
    leftBoundary = property(__leftBoundary.value, __leftBoundary.set, None, None)

    
    # Element rightBoundary uses Python identifier rightBoundary
    __rightBoundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rightBoundary'), 'rightBoundary', '__AbsentNamespace0_lanelet_rightBoundary', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 247, 12), )

    
    rightBoundary = property(__rightBoundary.value, __rightBoundary.set, None, None)

    
    # Element predecessor uses Python identifier predecessor
    __predecessor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predecessor'), 'predecessor', '__AbsentNamespace0_lanelet_predecessor', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 248, 12), )

    
    predecessor = property(__predecessor.value, __predecessor.set, None, None)

    
    # Element successor uses Python identifier successor
    __successor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'successor'), 'successor', '__AbsentNamespace0_lanelet_successor', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 250, 12), )

    
    successor = property(__successor.value, __successor.set, None, None)

    
    # Element adjacentLeft uses Python identifier adjacentLeft
    __adjacentLeft = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adjacentLeft'), 'adjacentLeft', '__AbsentNamespace0_lanelet_adjacentLeft', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 252, 12), )

    
    adjacentLeft = property(__adjacentLeft.value, __adjacentLeft.set, None, None)

    
    # Element adjacentRight uses Python identifier adjacentRight
    __adjacentRight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adjacentRight'), 'adjacentRight', '__AbsentNamespace0_lanelet_adjacentRight', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 254, 12), )

    
    adjacentRight = property(__adjacentRight.value, __adjacentRight.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_lanelet_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 257, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 257, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __leftBoundary.name() : __leftBoundary,
        __rightBoundary.name() : __rightBoundary,
        __predecessor.name() : __predecessor,
        __successor.name() : __successor,
        __adjacentLeft.name() : __adjacentLeft,
        __adjacentRight.name() : __adjacentRight
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.lanelet = lanelet
Namespace.addCategoryObject('typeBinding', 'lanelet', lanelet)


# Complex type egoVehicle with content type ELEMENT_ONLY
class egoVehicle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type egoVehicle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'egoVehicle')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 260, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_egoVehicle_type', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 262, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_egoVehicle_shape', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 263, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Element initialState uses Python identifier initialState
    __initialState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'initialState'), 'initialState', '__AbsentNamespace0_egoVehicle_initialState', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 264, 12), )

    
    initialState = property(__initialState.value, __initialState.set, None, None)

    
    # Element goalRegion uses Python identifier goalRegion
    __goalRegion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'goalRegion'), 'goalRegion', '__AbsentNamespace0_egoVehicle_goalRegion', False, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 265, 12), )

    
    goalRegion = property(__goalRegion.value, __goalRegion.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_egoVehicle_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 274, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 274, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __shape.name() : __shape,
        __initialState.name() : __initialState,
        __goalRegion.name() : __goalRegion
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.egoVehicle = egoVehicle
Namespace.addCategoryObject('typeBinding', 'egoVehicle', egoVehicle)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 266, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_CTD_ANON_4_state', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 268, 24), )

    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        __state.name() : __state
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type laneletAdjacentRef with content type EMPTY
class laneletAdjacentRef (pyxb.binding.basis.complexTypeDefinition):
    """Complex type laneletAdjacentRef with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'laneletAdjacentRef')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 238, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__AbsentNamespace0_laneletAdjacentRef_ref', pyxb.binding.datatypes.integer, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 239, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 239, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    
    # Attribute drivingDir uses Python identifier drivingDir
    __drivingDir = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'drivingDir'), 'drivingDir', '__AbsentNamespace0_laneletAdjacentRef_drivingDir', _module_typeBindings.drivingDir, required=True)
    __drivingDir._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 240, 8)
    __drivingDir._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 240, 8)
    
    drivingDir = property(__drivingDir.value, __drivingDir.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref,
        __drivingDir.name() : __drivingDir
    })
_module_typeBindings.laneletAdjacentRef = laneletAdjacentRef
Namespace.addCategoryObject('typeBinding', 'laneletAdjacentRef', laneletAdjacentRef)


# Complex type CommonRoad with content type ELEMENT_ONLY
class CommonRoad (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CommonRoad with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonRoad')
    _XSDLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 277, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element obstacle uses Python identifier obstacle
    __obstacle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'obstacle'), 'obstacle', '__AbsentNamespace0_CommonRoad_obstacle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 279, 12), )

    
    obstacle = property(__obstacle.value, __obstacle.set, None, None)

    
    # Element lanelet uses Python identifier lanelet
    __lanelet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanelet'), 'lanelet', '__AbsentNamespace0_CommonRoad_lanelet', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 281, 12), )

    
    lanelet = property(__lanelet.value, __lanelet.set, None, None)

    
    # Element egoVehicle uses Python identifier egoVehicle
    __egoVehicle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'egoVehicle'), 'egoVehicle', '__AbsentNamespace0_CommonRoad_egoVehicle', True, pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 283, 12), )

    
    egoVehicle = property(__egoVehicle.value, __egoVehicle.set, None, None)

    
    # Attribute commonRoadVersion uses Python identifier commonRoadVersion
    __commonRoadVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'commonRoadVersion'), 'commonRoadVersion', '__AbsentNamespace0_CommonRoad_commonRoadVersion', _module_typeBindings.STD_ANON, required=True)
    __commonRoadVersion._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 286, 8)
    __commonRoadVersion._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 286, 8)
    
    commonRoadVersion = property(__commonRoadVersion.value, __commonRoadVersion.set, None, None)

    
    # Attribute benchmarkID uses Python identifier benchmarkID
    __benchmarkID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'benchmarkID'), 'benchmarkID', '__AbsentNamespace0_CommonRoad_benchmarkID', pyxb.binding.datatypes.string)
    __benchmarkID._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 293, 8)
    __benchmarkID._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 293, 8)
    
    benchmarkID = property(__benchmarkID.value, __benchmarkID.set, None, None)

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__AbsentNamespace0_CommonRoad_date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 294, 8)
    __date._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 294, 8)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute timeStepSize uses Python identifier timeStepSize
    __timeStepSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeStepSize'), 'timeStepSize', '__AbsentNamespace0_CommonRoad_timeStepSize', pyxb.binding.datatypes.float)
    __timeStepSize._DeclarationLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 295, 8)
    __timeStepSize._UseLocation = pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 295, 8)
    
    timeStepSize = property(__timeStepSize.value, __timeStepSize.set, None, None)

    _ElementMap.update({
        __obstacle.name() : __obstacle,
        __lanelet.name() : __lanelet,
        __egoVehicle.name() : __egoVehicle
    })
    _AttributeMap.update({
        __commonRoadVersion.name() : __commonRoadVersion,
        __benchmarkID.name() : __benchmarkID,
        __date.name() : __date,
        __timeStepSize.name() : __timeStepSize
    })
_module_typeBindings.CommonRoad = CommonRoad
Namespace.addCategoryObject('typeBinding', 'CommonRoad', CommonRoad)


commonRoad = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'commonRoad'), CommonRoad, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 299, 4))
Namespace.addCategoryObject('elementBinding', commonRoad.name().localName(), commonRoad)



floatInterval._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'exact'), pyxb.binding.datatypes.float, scope=floatInterval, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 21, 12)))

floatInterval._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'intervalStart'), pyxb.binding.datatypes.float, scope=floatInterval, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 23, 16)))

floatInterval._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'intervalEnd'), pyxb.binding.datatypes.float, scope=floatInterval, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 24, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(floatInterval._UseForTag(pyxb.namespace.ExpandedName(None, 'exact')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(floatInterval._UseForTag(pyxb.namespace.ExpandedName(None, 'intervalStart')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 23, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(floatInterval._UseForTag(pyxb.namespace.ExpandedName(None, 'intervalEnd')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 24, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
floatInterval._Automaton = _BuildAutomaton()




point._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), pyxb.binding.datatypes.float, scope=point, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 38, 12)))

point._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), pyxb.binding.datatypes.float, scope=point, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 39, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(point._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(point._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
point._Automaton = _BuildAutomaton_()




rectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'length'), distance, scope=rectangle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 57, 12)))

rectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), distance, scope=rectangle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 58, 12)))

rectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=rectangle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 59, 12)))

rectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'centerPoint'), point, scope=rectangle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 60, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(rectangle._UseForTag(pyxb.namespace.ExpandedName(None, 'length')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 57, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(rectangle._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 58, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(rectangle._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 59, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(rectangle._UseForTag(pyxb.namespace.ExpandedName(None, 'centerPoint')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 60, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rectangle._Automaton = _BuildAutomaton_2()




circle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), distance, scope=circle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 76, 12)))

circle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'centerPoint'), point, scope=circle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 77, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(circle._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(circle._UseForTag(pyxb.namespace.ExpandedName(None, 'centerPoint')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 77, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
circle._Automaton = _BuildAutomaton_3()




polygon._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), point, scope=polygon, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 101, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 101, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(polygon._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 101, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
polygon._Automaton = _BuildAutomaton_4()




shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rectangle'), rectangle, scope=shape, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 119, 12)))

shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'circle'), circle, scope=shape, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 120, 12)))

shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'polygon'), polygon, scope=shape, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 121, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(shape._UseForTag(pyxb.namespace.ExpandedName(None, 'rectangle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 119, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(shape._UseForTag(pyxb.namespace.ExpandedName(None, 'circle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 120, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(shape._UseForTag(pyxb.namespace.ExpandedName(None, 'polygon')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 121, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
shape._Automaton = _BuildAutomaton_5()




occupancy._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shape'), shape, scope=occupancy, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 127, 12)))

occupancy._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time'), floatInterval, scope=occupancy, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 128, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(occupancy._UseForTag(pyxb.namespace.ExpandedName(None, 'shape')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 127, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(occupancy._UseForTag(pyxb.namespace.ExpandedName(None, 'time')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 128, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
occupancy._Automaton = _BuildAutomaton_6()




state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), CTD_ANON, scope=state, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 134, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), floatInterval, scope=state, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 146, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time'), floatInterval, scope=state, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 147, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), floatInterval, scope=state, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 148, 12)))

state._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'acceleration'), floatInterval, scope=state, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 149, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 148, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 149, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 146, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'time')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 147, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 148, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(state._UseForTag(pyxb.namespace.ExpandedName(None, 'acceleration')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 149, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
state._Automaton = _BuildAutomaton_7()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), point, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 137, 24)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rectangle'), rectangle, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 139, 28)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'circle'), circle, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 140, 28)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'polygon'), polygon, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 141, 28)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 137, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'rectangle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 139, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'circle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 140, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'polygon')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 141, 28))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_8()




obstacle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), obstacleRole, scope=obstacle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 179, 12)))

obstacle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), obstacleType, scope=obstacle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 180, 12)))

obstacle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shape'), shape, scope=obstacle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 181, 12)))

obstacle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trajectory'), CTD_ANON_, scope=obstacle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 183, 16)))

obstacle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'occupancySet'), CTD_ANON_2, scope=obstacle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 191, 16)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 182, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obstacle._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 179, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(obstacle._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 180, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(obstacle._UseForTag(pyxb.namespace.ExpandedName(None, 'shape')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 181, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(obstacle._UseForTag(pyxb.namespace.ExpandedName(None, 'trajectory')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 183, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(obstacle._UseForTag(pyxb.namespace.ExpandedName(None, 'occupancySet')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 191, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
obstacle._Automaton = _BuildAutomaton_9()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'state'), state, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 186, 28)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'state')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 186, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_10()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'occupancy'), occupancy, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 194, 28)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'occupancy')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 194, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_11()




boundary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), point, scope=boundary, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 213, 12)))

boundary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lineMarking'), lineMarking, scope=boundary, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 215, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 215, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(boundary._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 213, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(boundary._UseForTag(pyxb.namespace.ExpandedName(None, 'lineMarking')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 215, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
boundary._Automaton = _BuildAutomaton_12()




laneletRefList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanelet'), CTD_ANON_3, scope=laneletRefList, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 222, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(laneletRefList._UseForTag(pyxb.namespace.ExpandedName(None, 'lanelet')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 222, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
laneletRefList._Automaton = _BuildAutomaton_13()




lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'leftBoundary'), boundary, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 246, 12)))

lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rightBoundary'), boundary, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 247, 12)))

lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predecessor'), laneletRefList, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 248, 12)))

lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'successor'), laneletRefList, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 250, 12)))

lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adjacentLeft'), laneletAdjacentRef, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 252, 12)))

lanelet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adjacentRight'), laneletAdjacentRef, scope=lanelet, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 254, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 248, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 250, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 252, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 254, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'leftBoundary')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'rightBoundary')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 247, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'predecessor')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 248, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'successor')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 250, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'adjacentLeft')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 252, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(lanelet._UseForTag(pyxb.namespace.ExpandedName(None, 'adjacentRight')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 254, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
lanelet._Automaton = _BuildAutomaton_14()




egoVehicle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), obstacleType, scope=egoVehicle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 262, 12)))

egoVehicle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shape'), shape, scope=egoVehicle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 263, 12)))

egoVehicle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'initialState'), state, scope=egoVehicle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 264, 12)))

egoVehicle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'goalRegion'), CTD_ANON_4, scope=egoVehicle, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 265, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(egoVehicle._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 262, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(egoVehicle._UseForTag(pyxb.namespace.ExpandedName(None, 'shape')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 263, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(egoVehicle._UseForTag(pyxb.namespace.ExpandedName(None, 'initialState')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 264, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(egoVehicle._UseForTag(pyxb.namespace.ExpandedName(None, 'goalRegion')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 265, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
egoVehicle._Automaton = _BuildAutomaton_15()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'state'), state, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 268, 24)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'state')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 268, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_16()




CommonRoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'obstacle'), obstacle, scope=CommonRoad, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 279, 12)))

CommonRoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanelet'), lanelet, scope=CommonRoad, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 281, 12)))

CommonRoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'egoVehicle'), egoVehicle, scope=CommonRoad, location=pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 283, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonRoad._UseForTag(pyxb.namespace.ExpandedName(None, 'obstacle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 279, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonRoad._UseForTag(pyxb.namespace.ExpandedName(None, 'lanelet')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 281, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CommonRoad._UseForTag(pyxb.namespace.ExpandedName(None, 'egoVehicle')), pyxb.utils.utility.Location('/home/hans/thesis/extras/schema.xsd', 283, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CommonRoad._Automaton = _BuildAutomaton_17()

