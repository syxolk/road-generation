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
        <sensor type="camera" name="my_sensor">
          <pose>0 0 0.32 0 0.7 0</pose>
          <camera>
            <horizontal_fov>1.047</horizontal_fov>
            <image>
              <width>320</width>
              <height>240</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>100</far>
            </clip>
          </camera>
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
        </sensor>
      </link>
    </model>
    """.format(model_file)
