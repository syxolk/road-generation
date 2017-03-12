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

def generate_road(primitives_const, padding, curv_a):
    # add clothoids
    primitives = [primitives_const[0]]
    for i in range(1, len(primitives_const)):
        end_curv = primitives_const[i-1].get_ending()[2]
        begin_curv = primitives_const[i].get_beginning()[2]
        if abs(end_curv - begin_curv) > 0.001:
            primitives.append(primitive.Clothoid(end_curv, begin_curv, curv_a[i-1]))
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
        return angle_weight

def render_road(primitives):
    plt.axis('equal')
    plt.grid()
    for p in primitives:
        points = p.get_points()
        xvalues = list(map(lambda c: c[0], points))
        yvalues = list(map(lambda c: c[1], points))
        plt.plot(xvalues, yvalues, linewidth=3)
    plt.savefig("bla.png")
    plt.show()

def random_float_array(len, min, max):
    arr = []
    for i in range(len):
        arr.append(random.uniform(5, 15))
    return arr

def mutate(heap):
    mutate_heap = []

    for i in range(len(heap)):
        for j in range(10):
            curv_a = list(map(lambda x: x + random.uniform(-2, 2), heap[i][3]))
            road = generate_road(heap[i][2])
            h = f.fitness(road)
            mutate_heap.append((h, road, heap[i][2], curv_a))

    mutate_heap.sort(key=lambda x: x[0])

    best_n = 20
    best_heap = []
    for i in range(len(mutate_heap)):
        if check_intersections(mutate_heap[i][1], preset.road_width):
            continue
        else:
            best_heap.append(mutate_heap[i])
            best_n -= 1
            if best_n == 0:
                break

    return best_heap

if __name__ == "__main__":
    preset = preset_parser.parse(sys.argv[1])
    primitives = preset.primitives

    road = None
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        random.shuffle(primitives)
        curv_a = random_float_array(len(primitives), 10, 10)
        road = generate_road(primitives, 0, curv_a)
        if not check_intersections(road, preset.road_width):
            break
    print()

    render_road(road)
