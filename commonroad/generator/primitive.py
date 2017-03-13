import numpy as np
import math
from shapely.geometry import LineString, CAP_STYLE, JOIN_STYLE
import scipy.integrate as integrate
from commonroad import schema

class MissingPointsException(Exception):
    pass

def circle_from_points(x1, y1, x2, y2, x3, y3):
    s1 = np.array([[y2 - y1], [- (x2 - x1)]])
    s2 = np.array([[y3 - y2], [- (x3 - x2)]])
    mid1 = 0.5*np.array([[x1 + x2], [y1 + y2]])
    mid2 = 0.5*np.array([[x2 + x3], [y2 + y3]])
    b = mid2 - mid1
    A = np.hstack((s1, s2))
    if np.linalg.matrix_rank(A) == 2 :
        result = np.linalg.solve(A, b)
        circle_mid = mid1 + result[0] * s1
        radius = np.linalg.norm(circle_mid - [[x1], [y1]])
        return (circle_mid, radius)
    else:
        return None

def is_left(a, b, c):
    x = b - a
    y = c - a
    return np.cross(x, y) > 0

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
        points = self.get_points()
        p1 = np.array(points[0])
        p2 = np.array(points[1])
        dir = p1 - p2
        circle_mid, radius = circle_from_points(points[0][0], points[0][1],
            points[1][0], points[1][1], points[2][0], points[2][1])
        if not is_left(np.array(points[1]), np.array(points[0]), circle_mid.reshape(2)):
            radius = - radius # rechtskrümmung
        return (p1, math.atan2(dir[1], dir[0]), 1 / radius)

    def get_ending(self):
        points = self.get_points()
        p1 = np.array(points[-1])
        p2 = np.array(points[-2])
        dir = p1 - p2
        circle_mid, radius = circle_from_points(points[-1][0], points[-1][1],
            points[-2][0], points[-2][1], points[-3][0], points[-3][1])
        if not is_left(np.array(points[-2]), np.array(points[-1]), circle_mid.reshape(2)):
            radius = - radius # rechtskrümmung
        return (p1, math.atan2(dir[1], dir[0]), 1 / radius)

    def export(self, config):
        points = self.get_points()
        lanelet1 = schema.lanelet(leftBoundary=schema.boundary(), rightBoundary=schema.boundary())
        lanelet2 = schema.lanelet(leftBoundary=schema.boundary(), rightBoundary=schema.boundary())

        lanelet1.rightBoundary.lineMarking = "solid"
        lanelet1.leftBoundary.lineMarking = "dashed"
        lanelet2.rightBoundary.lineMarking = "solid"

        for i in range(len(points)-1):
            p1 = np.array(points[i])
            p2 = np.array(points[i+1])
            ortho_left = np.array([-(p2[1] - p1[1]), p2[0] - p1[0]])
            ortho_left = ortho_left / np.linalg.norm(ortho_left) * config.road_width
            ortho_right = ortho_left * (-1)

            left = p1 + ortho_left
            right = p1 + ortho_right

            lanelet1.leftBoundary.point.append(
                schema.point(x=points[i][0], y=points[i][1]))
            lanelet1.rightBoundary.point.append(
                schema.point(x=right[0], y=right[1]))
            lanelet2.leftBoundary.point.append(
                schema.point(x=points[i][0], y=points[i][1]))
            lanelet2.rightBoundary.point.append(
                schema.point(x=left[0], y=left[1]))
        # TODO add last point

        return [lanelet1, lanelet2]

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
        begin = self._child.get_beginning()
        return np.array([
            [cos, -sin, self._translation[0] + begin[0][0]],
            [sin, cos, self._translation[1] + begin[0][1]],
            [0, 0, 1]
        ]).dot(np.array([
            [1, 0, -begin[0][0]],
            [0, 1, -begin[0][1]],
            [0, 0, 1]
        ]))

    def _transform_point(self, point):
        return (self._get_matrix().dot(np.append(point, 1)))[0:2]

    def get_points(self):
        return list(map(self._transform_point, self._child.get_points()))

    def get_beginning(self):
        begin = self._child.get_beginning()
        return (self._transform_point(begin[0]), begin[1] + self._angle, begin[2])

    def get_ending(self):
        end = self._child.get_ending()
        return (self._transform_point(end[0]), end[1] + self._angle, end[2])

    def export(self, config):
        objects = self._child.export(config)

        for obj in objects:
            print("translate")
            if isinstance(obj, schema.lanelet):
                for i in range(len(obj.leftBoundary.point)):
                    x = obj.leftBoundary.point[i].x
                    y = obj.leftBoundary.point[i].y
                    transformed = self._transform_point([x, y])
                    obj.leftBoundary.point[i].x = transformed[0]
                    obj.leftBoundary.point[i].y = transformed[1]
                for i in range(len(obj.rightBoundary.point)):
                    x = obj.rightBoundary.point[i].x
                    y = obj.rightBoundary.point[i].y
                    transformed = self._transform_point([x, y])
                    obj.rightBoundary.point[i].x = transformed[0]
                    obj.rightBoundary.point[i].y = transformed[1]

        return objects

class StraightLine(Primitive):
    def __init__(self, length):
        self._length = length

    def __repr__(self):
        return "StraightLine(length={})".format(self._length)

    def get_points(self):
        return [[0, 0], [self._length, 0]]

    def get_beginning(self):
        return (np.array([0, 0]), math.pi, 0)

    def get_ending(self):
        return (np.array([self._length, 0]), 0, 0)

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
        return (np.array([0, 0]), math.pi, 1 / self._radius)

    def get_ending(self):
        return (np.array([
            math.cos(self._angle - math.pi/2) * self._radius,
            self._radius + math.sin(self._angle - math.pi/2) * self._radius
        ]), self._angle, - 1 / self._radius)

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
        return (np.array([0, 0]), math.pi, - 1 / self._radius)

    def get_ending(self):
        return (np.array([
            math.cos(math.pi/2 - self._angle) * self._radius,
            - self._radius + math.sin(math.pi/2 - self._angle) * self._radius
        ]), - self._angle, 1 / self._radius)

class CubicBezier(Primitive):
    def __init__(self, p1, p2, p3):
        self._p0 = np.array([0, 0])
        self._p1 = np.array(p1)
        self._p2 = np.array(p2)
        self._p3 = np.array(p3)

        self._points = []
        t = 0
        while t <= 1:
            c0 = (1-t) * self._p0 + t * self._p1
            c1 = (1-t) * self._p1 + t * self._p2
            c2 = (1-t) * self._p2 + t * self._p3
            d0 = (1-t) * c0 + t * c1
            d1 = (1-t) * c1 + t * c2
            x = (1-t) * d0 + t * d1
            self._points.append(x)
            t += 0.01

    def get_points(self):
        return self._points

def euler_spiral(l, A):
    factor = A * math.sqrt(math.pi)
    return [factor * integrate.quad(lambda t: math.cos(math.pi * t * t / 2), 0, l)[0],
        factor * integrate.quad(lambda t: math.sin(math.pi * t * t / 2), 0, l)[0]]

class Clothoid(Primitive):
    def __init__(self, curvature_begin, curvature_end, a):
        self._curv_begin = curvature_begin
        self._curv_end = curvature_end
        self._a = a # clothoid parameter A

        len_begin = math.fabs(curvature_begin) * a / math.sqrt(math.pi)
        len_end = math.fabs(curvature_end) * a / math.sqrt(math.pi)

        begin_points = []
        for l in np.arange(-len_begin, 0, 0.01):
            p = euler_spiral(l, a)
            if curvature_begin < 0: # nach rechts drehen
                p[1] = - p[1] # -> y-achse spiegeln
            begin_points.append(p)
        end_points = []
        for l in np.arange(0, len_end, 0.01):
            p = euler_spiral(l, a)
            if curvature_end < 0:
                p[1] = - p[1]
            end_points.append(p)
        self._points = begin_points + end_points
        if len(self._points) < 2:
            print(curvature_begin, curvature_end, a)

    def get_points(self):
        return self._points

    def get_beginning(self):
        dir = np.array(self._points[0]) - np.array(self._points[1])
        return (np.array(self._points[0]), math.atan2(dir[1], dir[0]), self._curv_begin)

    def get_ending(self):
        dir = np.array(self._points[-1]) - np.array(self._points[-2])
        return (np.array(self._points[-1]), math.atan2(dir[1], dir[0]), self._curv_end)

class LeftTurnCrossing(Primitive):
    def __init__(self, size):
        self._size = size
        self._points = [
            [0, -size],
            [0, 0],
            [-size, 0]
        ]

    def get_points(self):
        return self._points

    def get_beginning(self):
        return (np.array([0, -self._size]), 1.5 * math.pi, 0)

    def get_ending(self):
        return (np.array([-self._size, 0]), math.pi, 0)

class RightTurnCrossing(Primitive):
    def __init__(self, size):
        self._size = size
        self._points = [
            [0, -size],
            [0, 0],
            [size, 0]
        ]

    def get_points(self):
        return self._points

    def get_beginning(self):
        return (np.array([0, -self._size]), 1.5 * math.pi, 0)

    def get_ending(self):
        return (np.array([self._size, 0]), 0, 0)
