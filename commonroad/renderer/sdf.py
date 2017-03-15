from commonroad.renderer import groundplane, obstacle
from commonroad import schema
from os import path

def generate_sdf(xml_file, target_dir):
    with open(xml_file, "r") as file:
        content = file.read()
    doc = schema.CreateFromDocument(content)

    content = groundplane.draw(doc, target_dir)
    for obst in doc.obstacle:
        content += obstacle.draw(obst)

    with open(path.join(target_dir, "world.sdf"), "w") as file:
        file.write("<sdf version='1.6'><world name='default'>")
        file.write(content)
        file.write("</world></sdf>")
