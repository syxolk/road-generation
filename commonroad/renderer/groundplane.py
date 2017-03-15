#import cairo
import cairocffi as cairo
import math
from commonroad import utils
from os import path
import os
import hashlib
from tqdm import tqdm

PIXEL_PER_UNIT = 500
TILE_SIZE = 2048
PADDING = 3

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

def draw(doc, target_dir):
    bounding_box = utils.get_bounding_box(doc)
    bounding_box.x_min -= PADDING
    bounding_box.y_min -= PADDING
    bounding_box.x_max += PADDING
    bounding_box.y_max += PADDING
    print(bounding_box)

    width = math.ceil((bounding_box.x_max - bounding_box.x_min) * PIXEL_PER_UNIT)
    height = math.ceil((bounding_box.y_max - bounding_box.y_min) * PIXEL_PER_UNIT)

    width_num = math.ceil(width / TILE_SIZE)
    height_num = math.ceil(height / TILE_SIZE)

    os.makedirs(path.join(target_dir, "materials", "textures"), exist_ok=True)
    os.makedirs(path.join(target_dir, "materials", "scripts"), exist_ok=True)

    models = ""

    for (x, y) in tqdm([(x,y) for x in range(width_num) for y in range(height_num)]):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, TILE_SIZE, TILE_SIZE)
        ctx = cairo.Context(surface)

        # fill black
        ctx.set_source_rgb(0, 0, 0)
        ctx.rectangle(0, 0, TILE_SIZE, TILE_SIZE)
        ctx.fill()

        # Inverse y-axis
        ctx.translate(0, TILE_SIZE / 2)
        ctx.scale(1, -1)
        ctx.translate(0, -TILE_SIZE / 2)

        ctx.scale(PIXEL_PER_UNIT, PIXEL_PER_UNIT)
        ctx.translate(-bounding_box.x_min, -bounding_box.y_min)
        ctx.translate(- x * TILE_SIZE / PIXEL_PER_UNIT, - y * TILE_SIZE / PIXEL_PER_UNIT)

        ctx.set_source_rgb(1, 1, 1)
        for lanelet in doc.lanelet:
            draw_boundary(ctx, lanelet.leftBoundary)
            draw_boundary(ctx, lanelet.rightBoundary)
            draw_stop_line(ctx, lanelet)

        for obstacle in doc.obstacle:
            draw_obstacle(ctx, obstacle)

        sha_1 = hashlib.sha1()
        sha_1.update(surface.get_data())
        hash = sha_1.hexdigest()

        texture_file = "tile-{0}.png".format(hash)
        material_file = "tile-{0}.material".format(hash)
        surface.write_to_png(
            path.join(target_dir, "materials", "textures", texture_file))

        with open(path.join(target_dir, "materials", "scripts", material_file), "w") as file:
            file.write(ground_plane_material("Tile/" + hash, texture_file))

        models += ground_plane_model(
            bounding_box.x_min + (x + 0.5) * TILE_SIZE / PIXEL_PER_UNIT,
            bounding_box.y_min + (y + 0.5) * TILE_SIZE / PIXEL_PER_UNIT,
            TILE_SIZE / PIXEL_PER_UNIT,
            "Tile/{0}-{1}".format(x, y),
            "Tile/" + hash)

    return models

def ground_plane_material(name, file):
    return """
    material {name}
    {{
        technique
        {{
            pass
            {{
                ambient 0.5 0.5 0.5 1.0
                diffuse 1.0 1.0 1.0 1.0
                specular 0.0 0.0 0.0 1.0 0.5

                texture_unit
                {{
                    texture {file}
                    filtering anisotropic
                }}
            }}
        }}
    }}
    """.format(name=name, file=file)

def ground_plane_model(x, y, tile_size, name, material):
    return """
    <model name='{name}'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>{tile_size} {tile_size}</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>{tile_size} {tile_size}</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://materials/scripts</uri>
              <uri>file://materials/textures</uri>
              <name>{material}</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <pose frame=''>{x} {y} 0 0 -0 0</pose>
    </model>
    """.format(x=x, y=y, tile_size=tile_size, name=name, material=material)
