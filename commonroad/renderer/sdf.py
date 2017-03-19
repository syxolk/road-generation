from commonroad.renderer import groundplane, obstacle, traffic_sign
from commonroad import schema
from os import path

def generate_sdf(xml_content, target_dir):
    doc = schema.CreateFromDocument(xml_content)

    content = groundplane.draw(doc, target_dir)
    for obst in doc.obstacle:
        if obst.type != "blockedArea":
            content += obstacle.draw(obst)
    for sign in doc.trafficSign:
        content += traffic_sign.draw(sign, target_dir)

    with open(path.join(target_dir, "world.sdf"), "w") as file:
        file.write("<sdf version='1.6'><world name='default'>")
        file.write(content)
        file.write("</world></sdf>")
