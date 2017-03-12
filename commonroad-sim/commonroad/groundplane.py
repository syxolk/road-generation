from parser import Parser
import cairo
import math

PIXEL_PER_UNIT = 5000

def draw_boundary(ctx, points, marking):
    if marking is None:
        return
    ctx.set_line_width (0.02)
    if marking == "dashed":
        ctx.set_dash([0.2, 0.2])

    ctx.move_to(points[0].x, points[0].y)
    for p in points:
        ctx.line_to(p.x, p.y)

    ctx.stroke()

if __name__ == "__main__":
    parser = Parser()
    road = parser.parse("/home/hans/workspace/thesis/extras/example_lanelet.xml")
    bounding_box = road.get_bounding_box()

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
    for lanelet in road.get_lanelets():
        draw_boundary(ctx, lanelet.left_boundary, lanelet.left_boundary_marking)
        draw_boundary(ctx, lanelet.right_boundary, lanelet.right_boundary_marking)

    surface.write_to_png("example.png")
