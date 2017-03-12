from lxml import etree
from commonroad import CommonRoad, Point, Lanelet

class Parser:
    def __init__(self):
        pass

    def parse(self, file):
        tree = etree.parse(file)
        road = CommonRoad()

        for child in tree.getroot():
            id = int(child.get("id"))
            road_element = None

            if child.tag == "lanelet":
                left = []
                right = []
                for point in child.find("leftBoundary").findall("point"):
                    left.append(Point(float(point.find("x").text), float(point.find("y").text)))
                for point in child.find("rightBoundary").findall("point"):
                    right.append(Point(float(point.find("x").text), float(point.find("y").text)))

                left_line_marking = None
                right_line_marking = None
                if child.find("leftBoundary").find("lineMarking") is not None:
                    left_line_marking = child.find("leftBoundary").find("lineMarking").text
                if child.find("rightBoundary").find("lineMarking") is not None:
                    right_line_marking = child.find("rightBoundary").find("lineMarking").text
                road_element = Lanelet(left, right, left_line_marking, right_line_marking)

            if road_element is not None:
                road.add(id, road_element)
        return road
