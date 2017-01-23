import primitive
import preset_parser
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

def norm_angle(angle):
    while angle > 2 * math.pi:
        angle -= 2 * math.pi
    while angle < 0:
        angle += 2 * math.pi
    return angle

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
    x = np.array(b) - np.array(a)
    y = np.array(c) - np.array(a)
    return np.cross(x, y) > 0

def generate_road(primitives_const, padding):
    # add clothoids
    primitives = [primitives_const[0]]
    for i in range(1, len(primitives_const)):
        end_curv = primitives_const[i-1].get_ending()[2]
        begin_curv = primitives_const[i].get_beginning()[2]
        if abs(end_curv - begin_curv) > 0.01:
            primitives.append(primitive.Clothoid(end_curv, begin_curv, 10))
        primitives.append(primitives_const[i])

    new_primitives = [primitives[0]]

    for i in range(1, len(primitives)):
        last_primitive = new_primitives[i-1]
        current_primitive = primitives[i]

        (point, angle, curv) = last_primitive.get_ending()
        target_point = point + np.array([
            math.cos(angle) * padding,
            math.sin(angle) * padding
        ])
        #print(target_point)
        target_angle = norm_angle(angle + math.pi)
        #print(target_angle)
        (begin_point, begin_angle, begin_curv) = current_primitive.get_beginning()
        #print(begin_angle)
        new_primitives.append(primitive.TransrotPrimitive(current_primitive,
            target_point - begin_point, target_angle - begin_angle))
        #print(new_primitives)

    return new_primitives

def check_intersections(road, road_width):
    for i in range(len(road)-1):
        for j in range(i+2, len(road)):
            p1 = road[i].get_bounding_box(road_width)
            p2 = road[j].get_bounding_box(road_width)
            if p1.intersects(p2):
                return True
    return False

class Fitness:
    def __init__(self, target_distance):
        self._target_distance = target_distance

    def fitness(self, primitives):
        first_begin = primitives[0].get_beginning()
        last_end = primitives[-1].get_ending()
        dist_vec = first_begin[0] - last_end[0]
        dist = math.sqrt(dist_vec[0]*dist_vec[0] + dist_vec[1]*dist_vec[1])
        dist_weight = abs(dist - self._target_distance) / self._target_distance
        angle_weight = norm_angle(abs(norm_angle(first_begin[1]) - norm_angle(last_end[1] + math.pi))) / (2*math.pi)
        return dist_weight + angle_weight

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
    preset = preset_parser.parse(sys.argv[1])
    primitives = preset.primitives

    heap = []
    f = Fitness(1)
    for i in range(1000):
        random.shuffle(primitives)
        road = generate_road(primitives, 0)
        h = f.fitness(road)
        heap.append((h, road))

    # sort for fitness
    heap.sort(key=lambda x: x[0])

    # render best three
    best_n = 3
    for i in range(len(heap)):
        if check_intersections(heap[i][1], preset.road_width):
            continue
        else:
            render_road(heap[i][1])
            best_n -= 1
            if best_n == 0:
                break
