import bpy

def apply_geometry_nodes_preset(obj):
    # Remove existing Geometry Nodes modifiers
    for m in obj.modifiers:
        if m.type == 'NODES':
            obj.modifiers.remove(m)

    mod = obj.modifiers.new(name='GeometryNodes', type='NODES')
    ng = bpy.data.node_groups.new(name='GeometryNodesPreset', type='GeometryNodeTree')
    mod.node_group = ng
    nodes = ng.nodes
    links = ng.links

    nodes.clear()

    node = nodes.new('NodeGroupInput')
    node.name = 'Group Input'
    node.location = (-802.7391967773438, 1.9426835775375366)
    node.width_hidden = 0.0
    node.label = ''
    node.use_custom_color = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'NodeGroupInput'
    node.bl_label = 'Group Input'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'GROUP_INPUT'
    node.bl_width_default = 140.0
    node.bl_width_min = 80.0
    node.bl_width_max = 400.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0

    node = nodes.new('ShaderNodeTexWave')
    node.name = 'Wave Texture'
    node.location = (-542.5701904296875, 14.04531478881836)
    node.width_hidden = 0.0
    node.label = ''
    node.use_custom_color = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = True
    node.bl_idname = 'ShaderNodeTexWave'
    node.bl_label = 'Wave Texture'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'TEX_WAVE'
    node.bl_width_default = 150.0
    node.bl_width_min = 120.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.wave_type = 'BANDS'
    node.bands_direction = 'X'
    node.rings_direction = 'X'
    node.wave_profile = 'SIN'

    node = nodes.new('NodeGroupOutput')
    node.name = 'Group Output'
    node.location = (200.0, 0.0)
    node.width_hidden = 0.0
    node.label = ''
    node.use_custom_color = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'NodeGroupOutput'
    node.bl_label = 'Group Output'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'GROUP_OUTPUT'
    node.bl_width_default = 140.0
    node.bl_width_min = 80.0
    node.bl_width_max = 400.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.is_active_output = True

    node = nodes.new('GeometryNodeBlurAttribute')
    node.name = 'Blur Attribute'
    node.location = (-267.89959716796875, 4.331886291503906)
    node.width_hidden = 0.0
    node.label = ''
    node.use_custom_color = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'GeometryNodeBlurAttribute'
    node.bl_label = 'Blur Attribute'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'BLUR_ATTRIBUTE'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.data_type = 'FLOAT'

    node = nodes.new('GeometryNodeCurveArc')
    node.name = 'Arc'
    node.location = (-39.507286071777344, -8.51278305053711)
    node.width_hidden = 0.0
    node.label = ''
    node.use_custom_color = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'GeometryNodeCurveArc'
    node.bl_label = 'Arc'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'CURVE_PRIMITIVE_ARC'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.mode = 'RADIUS'

        # Create links safely
    def safe_link(from_node_name, from_socket_name, to_node_name, to_socket_name):
        from_node = nodes.get(from_node_name)
        to_node = nodes.get(to_node_name)

        if from_node and to_node:
            out_socket = next((s for s in from_node.outputs if s.name == from_socket_name), None)
            in_socket = next((s for s in to_node.inputs if s.name == to_socket_name), None)

            if out_socket and in_socket:
                links.new(out_socket, in_socket)

    # Example usage
    safe_link('Group Input', 'Geometry', 'Wave Texture', 'Vector')
    safe_link('Wave Texture', 'Color', 'Blur Attribute', 'Value')
    safe_link('Blur Attribute', 'Value', 'Arc', 'Start')
    safe_link('Blur Attribute', 'Value', 'Arc', 'Resolution')
    safe_link('Arc', 'Curve', 'Group Output', 'Geometry')


for obj in bpy.context.selected_objects:
    apply_geometry_nodes_preset(obj)