import primitive
import math
import matplotlib.pyplot as plt
import numpy as np
import random

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
        #print(target_point)
        target_angle = norm_angle(angle + math.pi)
        #print(target_angle)
        (begin_point, begin_angle) = current_primitive.get_beginning()
        #print(begin_angle)
        new_primitives.append(primitive.TransrotPrimitive(current_primitive,
            target_point - begin_point, target_angle - begin_angle))
        print(new_primitives)

    return new_primitives

def render_road(primitives):
    plt.axis('equal')
    plt.grid()
    for p in primitives:
        points = p.get_points()
        xvalues = list(map(lambda c: c[0], points))
        yvalues = list(map(lambda c: c[1], points))
        plt.plot(xvalues, yvalues, linewidth=3)
    plt.show()

if __name__ == "__main__":
    primitives = [
        primitive.StraightLine(5),
        primitive.CircularArc(10, math.pi ),
        primitive.StraightLine(10),
        primitive.CircularArc(5, math.pi/2 ),
        primitive.StraightLine(5)
        #primitive.CircularArc(10, math.pi * 0.5)
        #primitive.StraightLine(20),
    ]
    render_road(generate_road(primitives, 5))
    for i in range(5):
        random.shuffle(primitives)
        render_road(generate_road(primitives, 5))
