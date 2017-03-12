#!/usr/bin/env python3
import sys
from commonroad.renderer import groundplane
from commonroad import schema

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        content = file.read()
    doc = schema.CreateFromDocument(content)
    print(type(doc))

    groundplane.draw(doc).write_to_png("example.png")
