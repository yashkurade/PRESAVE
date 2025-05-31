import bpy

def apply_geometry_nodes_preset(obj):
    for m in obj.modifiers:
        if m.type == 'NODES':
            obj.modifiers.remove(m)

    mod = obj.modifiers.new(name='GeometryNodes', type='NODES')
    ng = bpy.data.node_groups.new(name='Geometry Nodes_Preset', type='GeometryNodeTree')
    mod.node_group = ng
    nodes = ng.nodes
    links = ng.links
    nodes.clear()

    node_0 = nodes.new('NodeGroupInput')
    node_0.name = 'Group Input'
    node_0.location = (-802.7391967773438, 1.9426835775375366)
    node_0.width_hidden = 0.0
    node_0.label = ''
    node_0.use_custom_color = False
    node_0.show_options = True
    node_0.show_preview = False
    node_0.hide = False
    node_0.mute = False
    node_0.show_texture = False
    node_0.bl_idname = 'NodeGroupInput'
    node_0.bl_label = 'Group Input'
    node_0.bl_description = ''
    node_0.bl_icon = 'NONE'
    node_0.bl_static_type = 'GROUP_INPUT'
    node_0.bl_width_default = 140.0
    node_0.bl_width_min = 80.0
    node_0.bl_width_max = 400.0
    node_0.bl_height_default = 100.0
    node_0.bl_height_min = 30.0
    node_0.bl_height_max = 30.0

    node_1 = nodes.new('ShaderNodeTexWave')
    node_1.name = 'Wave Texture'
    node_1.location = (-542.5701904296875, 14.04531478881836)
    node_1.width_hidden = 0.0
    node_1.label = ''
    node_1.use_custom_color = False
    node_1.show_options = True
    node_1.show_preview = False
    node_1.hide = False
    node_1.mute = False
    node_1.show_texture = True
    node_1.bl_idname = 'ShaderNodeTexWave'
    node_1.bl_label = 'Wave Texture'
    node_1.bl_description = ''
    node_1.bl_icon = 'NONE'
    node_1.bl_static_type = 'TEX_WAVE'
    node_1.bl_width_default = 150.0
    node_1.bl_width_min = 120.0
    node_1.bl_width_max = 700.0
    node_1.bl_height_default = 100.0
    node_1.bl_height_min = 30.0
    node_1.bl_height_max = 30.0
    node_1.wave_type = 'BANDS'
    node_1.bands_direction = 'X'
    node_1.rings_direction = 'X'
    node_1.wave_profile = 'SIN'

    node_2 = nodes.new('NodeGroupOutput')
    node_2.name = 'Group Output'
    node_2.location = (200.0, 0.0)
    node_2.width_hidden = 0.0
    node_2.label = ''
    node_2.use_custom_color = False
    node_2.show_options = True
    node_2.show_preview = False
    node_2.hide = False
    node_2.mute = False
    node_2.show_texture = False
    node_2.bl_idname = 'NodeGroupOutput'
    node_2.bl_label = 'Group Output'
    node_2.bl_description = ''
    node_2.bl_icon = 'NONE'
    node_2.bl_static_type = 'GROUP_OUTPUT'
    node_2.bl_width_default = 140.0
    node_2.bl_width_min = 80.0
    node_2.bl_width_max = 400.0
    node_2.bl_height_default = 100.0
    node_2.bl_height_min = 30.0
    node_2.bl_height_max = 30.0
    node_2.is_active_output = True

    node_3 = nodes.new('GeometryNodeBlurAttribute')
    node_3.name = 'Blur Attribute'
    node_3.location = (-267.89959716796875, 4.331886291503906)
    node_3.width_hidden = 0.0
    node_3.label = ''
    node_3.use_custom_color = False
    node_3.show_options = True
    node_3.show_preview = False
    node_3.hide = False
    node_3.mute = False
    node_3.show_texture = False
    node_3.bl_idname = 'GeometryNodeBlurAttribute'
    node_3.bl_label = 'Blur Attribute'
    node_3.bl_description = ''
    node_3.bl_icon = 'NONE'
    node_3.bl_static_type = 'BLUR_ATTRIBUTE'
    node_3.bl_width_default = 140.0
    node_3.bl_width_min = 100.0
    node_3.bl_width_max = 700.0
    node_3.bl_height_default = 100.0
    node_3.bl_height_min = 30.0
    node_3.bl_height_max = 30.0
    node_3.data_type = 'FLOAT'

    node_4 = nodes.new('GeometryNodeCurveArc')
    node_4.name = 'Arc'
    node_4.location = (-39.507286071777344, -8.51278305053711)
    node_4.width_hidden = 0.0
    node_4.label = ''
    node_4.use_custom_color = False
    node_4.show_options = True
    node_4.show_preview = False
    node_4.hide = False
    node_4.mute = False
    node_4.show_texture = False
    node_4.bl_idname = 'GeometryNodeCurveArc'
    node_4.bl_label = 'Arc'
    node_4.bl_description = ''
    node_4.bl_icon = 'NONE'
    node_4.bl_static_type = 'CURVE_PRIMITIVE_ARC'
    node_4.bl_width_default = 140.0
    node_4.bl_width_min = 100.0
    node_4.bl_width_max = 700.0
    node_4.bl_height_default = 100.0
    node_4.bl_height_min = 30.0
    node_4.bl_height_max = 30.0
    node_4.mode = 'RADIUS'

    # Create links
    links.new(node_0.outputs['Geometry'], node_1.inputs['Vector'])
    links.new(node_1.outputs['Color'], node_3.inputs['Value'])
    links.new(node_3.outputs['Value'], node_4.inputs['Start'])
    links.new(node_4.outputs['Curve'], node_2.inputs['Geometry'])
    links.new(node_3.outputs['Value'], node_4.inputs['Resolution'])

for obj in bpy.context.selected_objects:
    apply_geometry_nodes_preset(obj)