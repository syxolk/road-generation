#!/usr/bin/env python3
import sys, argparse
from commonroad import schema
from commonroad.generator import road_generation, preset_parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a randomized CommonRoad XML from a preset file")
    parser.add_argument("input", nargs="?", type=argparse.FileType("r"),
        default=sys.stdin)
    parser.add_argument("--output", "-o", type=argparse.FileType("w"),
        default=sys.stdout)
    args = parser.parse_args()

    with args.input as input_file:
        preset_data = input_file.read()

    preset = preset_parser.parse(preset_data)
    primitives = road_generation.generate(preset)

    doc = schema.commonRoad()
    doc.commonRoadVersion = "1.0"
    id = 0
    for p in primitives:
        objects = p.export(preset)
        for obj in objects:
            id -= 1
            obj.id = id
            doc.append(obj)

    with args.output as file:
        file.write(doc.toxml())
