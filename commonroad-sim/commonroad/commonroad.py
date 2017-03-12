from functools import reduce

class BoundingBox:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def union(self, box):
        return BoundingBox(
            min(self.x_min, box.x_min),
            min(self.y_min, box.y_min),
            max(self.x_max, box.x_max),
            max(self.y_max, box.y_max))

    def __repr__(self):
        return "BoundingBox({0}, {1}, {2}, {3})".format(self.x_min, self.y_min,
            self.x_max, self.y_max)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

class Lanelet:
    def __init__(self, left_boundary, right_boundary, left_boundary_marking, right_boundary_marking):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.left_boundary_marking = left_boundary_marking
        self.right_boundary_marking = right_boundary_marking

    def get_bounding_box(self):
        all_x = list(map(lambda p: p.x, self.left_boundary)) + list(map(lambda p: p.x, self.right_boundary))
        all_y = list(map(lambda p: p.y, self.left_boundary)) + list(map(lambda p: p.y, self.right_boundary))
        return BoundingBox(min(all_x), min(all_y), max(all_x), max(all_y))

    def __repr__(self):
        return "Lanelet({0}, {1})".format(self.left_boundary,
            self.right_boundary)

class CommonRoad:
    def __init__(self):
        self._elements = {}
        self._lanelets = []

    def add(self, id, element):
        if not isinstance(id, int):
            raise ValueError("id is not an integer: {0}".format(id))
        if isinstance(element, Lanelet):
            self._elements[id] = element
            self._lanelets.append(element)

    def get(self, id):
        return self._elements[id]

    def get_lanelets(self):
        return self._lanelets

    def get_bounding_box(self):
        return reduce(lambda x,y: x.union(y), map(lambda key: self._elements[key].get_bounding_box(), self._elements))
