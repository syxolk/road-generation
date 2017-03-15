import ruamel.yaml as yaml
from commonroad.generator import primitive
import math

class Preset:
    def __init__(self):
        # set sensitve defaults
        self.road_width = 1
        self.default_paddding = 2
        self.primitives = []

def parse(path):
    with open(path, "r") as file:
        data = yaml.load(file, Loader=yaml.RoundTripLoader)
    preset = Preset()
    preset.road_width = data["road_width"]
    for p in data["primitives"]:
        if "straight_line" in p:
            preset.primitives.append(
                primitive.StraightLine(p["straight_line"]["length"]))
        elif "right_arc" in p:
            preset.primitives.append(primitive.RightCircularArc(
                p["right_arc"]["radius"],
                math.radians(p["right_arc"]["angle"])))
        elif "left_arc" in p:
            preset.primitives.append(primitive.LeftCircularArc(
                p["left_arc"]["radius"],
                math.radians(p["left_arc"]["angle"])))
        elif "cubic_bezier" in p:
            data = p["cubic_bezier"]
            preset.primitives.append(primitive.CubicBezier(
                data["p1"], data["p2"], data["p3"]))
        elif "clothoid" in p:
            data = p["clothoid"]
            preset.primitives.append(primitive.Clothoid(
                data["curv1"], data["curv2"], data["a"]))
        elif "left_turn_crossing" in p:
            data = p["left_turn_crossing"]
            preset.primitives.append(primitive.LeftTurnCrossing(
                data["size"]))
        elif "right_turn_crossing" in p:
            data = p["right_turn_crossing"]
            preset.primitives.append(primitive.RightTurnCrossing(
                data["size"]))
        elif "obstacle" in p:
            data = p["obstacle"]
            preset.primitives.append(primitive.StraightLineObstacle(
                data["length"], data["obstacle_size"], data["lane"]
            ))
        else:
            raise ValueError("Unknown primitive type")
    return preset
