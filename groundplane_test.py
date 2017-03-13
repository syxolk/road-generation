#!/usr/bin/env python3
from commonroad.renderer import sdf
import sys

if __name__ == "__main__":
    sdf.generate_sdf(sys.argv[1], sys.argv[2])
