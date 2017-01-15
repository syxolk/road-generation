import numpy as np
import math

class MissingPointsException(Exception):
    pass

class Primitive:
    def get_points(self):
        return []

    def get_bounding_box(self):
        points = self.get_points()
        if len(points) == 0:
            raise MissingPointsException("get_points() returned empty array")
        return (
            [np.min(self.get_points()[:][0]), np.min(self.get_points()[:][1])],
            [np.max(self.get_points()[:][0]), np.max(self.get_points()[:][1])]
        )

    def get_open_ends():
        return np.array([])

class TransrotPrimitive(Primitive):
    def __init__(self, child):
        self._child = child
        self._angle = 0
        self._translation = np.array([0, 0])

    def get_angle(self):
        return self._angle

    def set_angle(self, angle):
        self._angle = angle

    angle = property(get_angle, set_angle)

    def _get_matrix(self):
        cos = math.cos(self._angle)
        sin = math.sin(self._angle)
        return np.array([
            [cos, -sin, self._translation[0]],
            [sin, cos, self._translation[1]],
            [0, 0, 1]
        ])

    def _transform_point(self, point):
        return (self._get_matrix() * np.append(point, 1))[0:2]

    def get_bounding_box(self):
        bb = self._child.get_bounding_box()
        m = self._get_matrix()
        return (
            (m * np.append(bb[0], 1))[0:2],
            (m * np.append(bb[1], 1))[0:2]
        )

    def get_points(self):
        return map(self._transform_point, self._child.get_points())

class StraightLine(Primitive):
    def __init__(self, length):
        self._length = length

    def get_points(self):
        return [[0, 0], [0, self._length]]

class CircularArc(Primitive):
    def __init__(self, radius, angle):
        self._radius = radius
        self._angle = angle

    def get_points(self):
        points = []
        current_angle = 0
        while current_angle <= self._angle:
            points.append([
                math.cos(self._angle) * self._radius,
                math.sin(self._angle) * self._radius
            ])
            current_angle += 0.1
        return points

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
