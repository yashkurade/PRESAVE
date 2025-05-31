import bpy
from mathutils import Color

def apply_material_preset(obj):
    mat = bpy.data.materials.new(name='gradiento')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    node = nodes.new('ShaderNodeOutputMaterial')
    node.name = 'Material Output'
    node.location = (300.0, 300.0)
    node.width = 140.0
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.608000, 0.608000, 0.608000))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_label = 'Material Output'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'OUTPUT_MATERIAL'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.is_active_output = True
    node.target = 'ALL'

    node = nodes.new('ShaderNodeBsdfPrincipled')
    node.name = 'Principled BSDF'
    node.location = (10.0, 300.0)
    node.width = 240.0
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.608000, 0.608000, 0.608000))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_label = 'Principled BSDF'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'BSDF_PRINCIPLED'
    node.bl_width_default = 240.0
    node.bl_width_min = 140.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.distribution = 'GGX'
    node.subsurface_method = 'RANDOM_WALK'

    node = nodes.new('ShaderNodeTexGradient')
    node.name = 'Gradient Texture'
    node.location = (-592.47705078125, 204.7315673828125)
    node.width = 140.0
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.608000, 0.608000, 0.608000))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = True
    node.bl_label = 'Gradient Texture'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'TEX_GRADIENT'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.gradient_type = 'LINEAR'

    node = nodes.new('ShaderNodeValToRGB')
    node.name = 'Color Ramp'
    node.location = (-338.2054443359375, 199.7116241455078)
    node.width = 240.0
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.608000, 0.608000, 0.608000))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_label = 'Color Ramp'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'VALTORGB'
    node.bl_width_default = 240.0
    node.bl_width_min = 140.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0

    node = nodes.new('ShaderNodeTexCoord')
    node.name = 'Texture Coordinate'
    node.location = (-915.639892578125, 179.63185119628906)
    node.width = 140.0
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.608000, 0.608000, 0.608000))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_label = 'Texture Coordinate'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'TEX_COORD'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node.object = None
    node.from_instancer = False

    links.new(nodes['Principled BSDF'].outputs['BSDF'], nodes['Material Output'].inputs['Surface'])
    links.new(nodes['Texture Coordinate'].outputs['Object'], nodes['Gradient Texture'].inputs['Vector'])
    links.new(nodes['Gradient Texture'].outputs['Color'], nodes['Color Ramp'].inputs['Fac'])
    links.new(nodes['Color Ramp'].outputs['Color'], nodes['Principled BSDF'].inputs['Base Color'])

    # Assign material to object
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

apply_material_preset(bpy.context.active_object)