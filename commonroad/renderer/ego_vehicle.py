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
        <collision name="collision">
          <pose>0.11 0 0.04  0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.2 0.08</size>
            </box>
          </geometry>
        </collision>
        <sensor type="camera" name="my_sensor">
          <pose>0 0 0.32 0 0.7 0</pose>
          <camera>
            <horizontal_fov>2.0</horizontal_fov>
            <image>
              <width>640</width>
              <height>480</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>100</far>
            </clip>
            <lens>
              <type>gnomonical</type>
              <scale_to_hfov>true</scale_to_hfov>
              <cutoff_angle>2.4</cutoff_angle>
              <env_texture_size>512</env_texture_size>
            </lens>
          </camera>
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
        </sensor>
      </link>
      <plugin name="push_animate" filename="libanimated_box.so"/>
    </model>
    """.format(model_file)
