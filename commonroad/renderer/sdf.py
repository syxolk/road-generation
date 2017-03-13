from commonroad.renderer import groundplane
from commonroad import schema
from os import path

def generate_sdf(xml_file, target_dir):
    with open(xml_file, "r") as file:
        content = file.read()
    doc = schema.CreateFromDocument(content)

    gp = groundplane.draw(doc, target_dir)

    with open(path.join(target_dir, "world.sdf"), "w") as file:
        file.write("<sdf version='1.6'><world name='default'>")
        file.write(gp)
        file.write("</world></sdf>")
