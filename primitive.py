import numpy as np
import math
from shapely.geometry import LineString, CAP_STYLE, JOIN_STYLE

class MissingPointsException(Exception):
    pass

class Primitive:
    def get_points(self):
        return []

    def get_bounding_box(self, street_width):
        points = self.get_points()
        if len(points) == 0:
            raise MissingPointsException("get_points() returned empty array")
        line = LineString(points)
        polygon = line.buffer(street_width, cap_style=CAP_STYLE.flat, join_style=JOIN_STYLE.round)
        return polygon

    def get_beginning(self):
        raise NotImplementedError()

    def get_ending(self):
        raise NotImplementedError()

class TransrotPrimitive(Primitive):
    def __init__(self, child, translation, angle):
        self._child = child
        self._angle = angle
        self._translation = translation

    def __repr__(self):
        return "TransrotPrimitive(translation={}, angle={}, child={})".format(
            self._translation, self._angle, self._child)

    def _get_matrix(self):
        cos = math.cos(self._angle)
        sin = math.sin(self._angle)
        return np.array([
            [cos, -sin, self._translation[0]],
            [sin, cos, self._translation[1]],
            [0, 0, 1]
        ])

    def _transform_point(self, point):
        return (self._get_matrix().dot(np.append(point, 1)))[0:2]

    def get_points(self):
        return list(map(self._transform_point, self._child.get_points()))

    def get_beginning(self):
        begin = self._child.get_beginning()
        return (self._transform_point(begin[0]), begin[1] + self._angle)

    def get_ending(self):
        end = self._child.get_ending()
        return (self._transform_point(end[0]), end[1] + self._angle)

class StraightLine(Primitive):
    def __init__(self, length):
        self._length = length

    def __repr__(self):
        return "StraightLine(length={})".format(self._length)

    def get_points(self):
        return [[0, 0], [self._length, 0]]

    def get_beginning(self):
        return (np.array([0, 0]), math.pi)

    def get_ending(self):
        return (np.array([self._length, 0]), 0)

class LeftCircularArc(Primitive):
    def __init__(self, radius, angle):
        self._radius = radius
        self._angle = angle

    def __repr__(self):
        return "LeftCircularArc(radius={}, angle={})".format(self._radius, self._angle)

    def get_points(self):
        points = []
        current_angle = 0
        while current_angle <= self._angle:
            points.append([
                math.cos(current_angle - math.pi/2) * self._radius,
                self._radius + math.sin(current_angle - math.pi/2) * self._radius
            ])
            current_angle += 0.01 # TODO what else
        return points

    def get_beginning(self):
        return (np.array([0, 0]), math.pi)

    def get_ending(self):
        return (np.array([
            math.cos(self._angle - math.pi/2) * self._radius,
            self._radius + math.sin(self._angle - math.pi/2) * self._radius
        ]), self._angle)

class RightCircularArc(Primitive):
    def __init__(self, radius, angle):
        self._radius = radius
        self._angle = angle

    def __repr__(self):
        return "RightCircularArc(radius={}, angle={})".format(self._radius, self._angle)

    def get_points(self):
        points = []
        current_angle = 0
        while current_angle <= self._angle:
            points.append([
                math.cos(math.pi/2 - current_angle) * self._radius,
                - self._radius + math.sin(math.pi/2 - current_angle) * self._radius
            ])
            current_angle += 0.01 # TODO what else
        return points

    def get_beginning(self):
        return (np.array([0, 0]), math.pi)

    def get_ending(self):
        return (np.array([
            math.cos(math.pi/2 - self._angle) * self._radius,
            - self._radius + math.sin(math.pi/2 - self._angle) * self._radius
        ]), - self._angle)

class QuadBezier(Primitive): #TODO noch nicht fertig
    def __init__(self, p1, p2):
        self._p0 = np.array([0, 0])
        self._p1 = p1
        self._p2 = p2

    def get_points(self):
        points = []
        t = 0
        while t <= 1:
            a = (1-t) * self._p0 + t * self._p1
            b = (1-t) * self._p1 + t * self._p2
            x = (1-t) * a + t * b
            points.append(x)
            t += 0.01
        return np.array(points)
