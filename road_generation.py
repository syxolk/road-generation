import primitive
import math
import matplotlib.pyplot as plt
import numpy as np

def norm_angle(angle):
    while angle > 2 * math.pi:
        angle -= 2 * math.pi
    while angle < 0:
        angle += 2 * math.pi
    return angle

def generate_road(primitives, padding):
    new_primitives = [primitives[0]]

    for i in range(1, len(primitives)):
        last_primitive = new_primitives[i-1]
        current_primitive = primitives[i]

        (point, angle) = last_primitive.get_ending()
        target_point = point + np.array([
            math.cos(angle) * padding,
            math.sin(angle) * padding
        ])
        target_angle = norm_angle(angle + 2 * math.pi)
        (begin_point, begin_angle) = last_primitive.get_beginning()
        new_primitives.append(primitive.TransrotPrimitive(current_primitive,
            target_point - begin_point, target_angle - begin_angle))

    return new_primitives

def render_road(primitives):
    for p in primitives:
        points = p.get_points()
        xvalues = map(lambda c: c[0], points)
        yvalues = map(lambda c: c[1], points)
        plt.plot(xvalues, yvalues)
    plt.show()

if __name__ == "__main__":
    primitives = [
        primitive.StraightLine(10),
        primitive.CircularArc(10, math.pi),
        primitive.CircularArc(10, math.pi * 0.5),
        primitive.StraightLine(10)
    ]
    render_road(generate_road(primitives, 10))
