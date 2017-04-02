from commonroad.generator import primitive
import random

class Preset:
    def __init__(self):
        # set sensitve defaults
        self.road_width = 1
        self.primitives = []

def eval(root):
    preset = Preset()
    preset.road_width = 0.4 # TODO
    preset.primitives = eval_element(root.find("sequence"))
    return preset

def eval_element(el):
    if el.tag == "line":
        return [
            primitive.StraightLine(el.attrib)
        ]
    elif el.tag == "leftArc":
        return [
            primitive.LeftCircularArc(el.attrib)
        ]
    elif el.tag == "rightArc":
        return [
            primitive.RightCircularArc(el.attrib)
        ]
    elif el.tag == "quadBezier":
        return [
            primitive.QuadBezier(el.attrib)
        ]
    elif el.tag == "cubicBezier":
        return [
            primitive.CubicBezier(el.attrib)
        ]
    elif el.tag == "blockedArea":
        return [
            primitive.BlockedAreaObstacle(el.attrib)
        ]
    elif el.tag == "intersection":
        return [
            primitive.Intersection(el.attrib)
        ]
    elif el.tag == "staticObstacle":
        return [
            primitive.StraightLineObstacle(el.attrib)
        ]
    elif el.tag == "trafficSign":
        return [
            primitive.TrafficSign(el.attrib)
        ]
    elif el.tag == "sequence":
        return [x for child in el for x in eval_element(child)]
    elif el.tag == "optional":
        if random.random() < float(el.attrib["p"]):
            return [x for child in el for x in eval_element(child)]
        else:
            return []
    elif el.tag == "repeat":
        return [x for _ in range(int(el.attrib["n"])) for child in el for x in eval_element(child)]
    elif el.tag == "select":
        total = sum([float(case.attrib["p"]) for case in el])
        target = random.random() * total
        current_total = 0
        for case in el:
            current_total += float(case.attrib["p"])
            if target < current_total:
                return [x for child in case for x in eval_element(child)]
                break
    else:
        return []
