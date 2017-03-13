#!/usr/bin/env python3
import sys
from commonroad import schema
from commonroad.generator import road_generation
from commonroad.generator import preset_parser

if __name__ == "__main__":
    preset = preset_parser.parse(sys.argv[1])
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

    with open(sys.argv[2], "w") as file:
        file.write(doc.toxml())
