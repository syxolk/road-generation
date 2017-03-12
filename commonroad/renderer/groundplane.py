import cairo
import math
from commonroad import utils

PIXEL_PER_UNIT = 5000

def draw_boundary(ctx, boundary):
    if boundary.lineMarking is None:
        return
    ctx.set_line_width (0.02)
    if boundary.lineMarking == "dashed":
        ctx.set_dash([0.2, 0.2])

    ctx.move_to(boundary.point[0].x, boundary.point[0].y)
    for p in boundary.point:
        ctx.line_to(p.x, p.y)

    ctx.stroke()

def draw(doc):
    bounding_box = utils.get_bounding_box(doc)
    print(bounding_box)

    width = math.ceil((bounding_box.x_max - bounding_box.x_min) * PIXEL_PER_UNIT)
    height = math.ceil((bounding_box.y_max - bounding_box.y_min) * PIXEL_PER_UNIT)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(PIXEL_PER_UNIT, PIXEL_PER_UNIT)
    ctx.translate(-bounding_box.x_min, -bounding_box.y_min)

    ctx.set_source_rgb(0, 0, 0) # black
    ctx.rectangle(bounding_box.x_min, bounding_box.y_min,
        bounding_box.x_max - bounding_box.x_min,
        bounding_box.y_max - bounding_box.y_min)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    for lanelet in doc.lanelet:
        draw_boundary(ctx, lanelet.leftBoundary)
        draw_boundary(ctx, lanelet.rightBoundary)

    return surface
