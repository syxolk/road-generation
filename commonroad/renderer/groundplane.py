import cairo
import math
from commonroad import utils

PIXEL_PER_UNIT = 1000

def draw_boundary(ctx, boundary):
    if boundary.lineMarking is None:
        return
    ctx.set_line_width (0.02)
    if boundary.lineMarking == "dashed":
        ctx.set_dash([0.2, 0.2])
    else:
        ctx.set_dash([])

    ctx.move_to(boundary.point[0].x, boundary.point[0].y)
    for p in boundary.point[1:]:
        ctx.line_to(p.x, p.y)
    ctx.stroke()

def draw_stop_line(ctx, lanelet):
    p1 = lanelet.leftBoundary.point[-1]
    p2 = lanelet.rightBoundary.point[-1]

    if lanelet.stopLine:
        if lanelet.stopLine == "dashed":
            ctx.set_dash([0.1, 0.1])
        else:
            ctx.set_dash([])
        ctx.move_to(p1.x, p1.y)
        ctx.line_to(p2.x, p2.y)
        ctx.stroke()

def draw_rectangle(ctx, rectangle):
    ctx.save()
    ctx.translate(rectangle.centerPoint.x, rectangle.centerPoint.y)
    ctx.rotate(-rectangle.orientation)
    ctx.rectangle(- rectangle.width / 2, - rectangle.length / 2, rectangle.width, rectangle.length)
    ctx.fill()
    ctx.restore()

def draw_circle(ctx, circle):
    ctx.arc(circle.centerPoint.x, circle.centerPoint.y, circle.radius, 0, 2*math.pi)
    ctx.fill()

def draw_polygon(ctx, polygon):
    ctx.move_to(polygon.point[0].x, polygon.point[1].y)
    for point in polygon.point[1:]:
        ctx.line_to(point.x, point.y)
    ctx.fill()

def draw_shape(ctx, shape):
    for rect in shape.rectangle:
        draw_rectangle(ctx, rect)
    for circ in shape.circle:
        draw_circle(ctx, circ)
    for poly in shape.polygon:
        draw_polygon(ctx, poly)

def draw_obstacle(ctx, obstacle):
    draw_shape(ctx, obstacle.shape)

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
        draw_stop_line(ctx, lanelet)

    for obstacle in doc.obstacle:
        draw_obstacle(ctx, obstacle)

    return surface
