import shutil, pkg_resources, os

def draw(target_dir):
    model_file = "car-cc2017.dae"
    model_stream = pkg_resources.resource_stream("commonroad.renderer.models",
        model_file)
    with open(os.path.join(target_dir, model_file), "wb") as model_target:
        shutil.copyfileobj(model_stream, model_target)

    return """
    <model name="EgoVehicle">
      <pose>0 0 0  0 0 0</pose>
      <static>true</static>
      <link name="body">
        <visual name="visual">
          <geometry>
            <mesh><uri>file://{0}</uri></mesh>
          </geometry>
        </visual>
      </link>
    </model>
    """.format(model_file)
