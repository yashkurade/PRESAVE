import bpy
from mathutils import Color

def apply_material_preset(obj):
    mat = bpy.data.materials.new(name='testo')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    node_0 = nodes.new('ShaderNodeOutputMaterial')
    node_0.name = 'Material Output'
    node_0.location = (300.0, 300.0)
    node_0.width = 140.0
    node_0.width_hidden = 0.0
    node_0.height = 100.0
    node_0.label = ''
    node_0.use_custom_color = False
    node_0.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node_0.show_options = True
    node_0.show_preview = False
    node_0.hide = False
    node_0.mute = False
    node_0.show_texture = False
    node_0.bl_idname = 'ShaderNodeOutputMaterial'
    node_0.bl_label = 'Material Output'
    node_0.bl_description = ''
    node_0.bl_icon = 'NONE'
    node_0.bl_static_type = 'OUTPUT_MATERIAL'
    node_0.bl_width_default = 140.0
    node_0.bl_width_min = 100.0
    node_0.bl_width_max = 700.0
    node_0.bl_height_default = 100.0
    node_0.bl_height_min = 30.0
    node_0.bl_height_max = 30.0
    node_0.is_active_output = True
    node_0.target = 'ALL'

    node_1 = nodes.new('ShaderNodeBsdfPrincipled')
    node_1.name = 'Principled BSDF'
    node_1.location = (10.0, 300.0)
    node_1.width = 240.0
    node_1.width_hidden = 0.0
    node_1.height = 100.0
    node_1.label = ''
    node_1.use_custom_color = False
    node_1.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node_1.show_options = True
    node_1.show_preview = False
    node_1.hide = False
    node_1.mute = False
    node_1.show_texture = False
    node_1.bl_idname = 'ShaderNodeBsdfPrincipled'
    node_1.bl_label = 'Principled BSDF'
    node_1.bl_description = ''
    node_1.bl_icon = 'NONE'
    node_1.bl_static_type = 'BSDF_PRINCIPLED'
    node_1.bl_width_default = 240.0
    node_1.bl_width_min = 140.0
    node_1.bl_width_max = 700.0
    node_1.bl_height_default = 100.0
    node_1.bl_height_min = 30.0
    node_1.bl_height_max = 30.0
    node_1.distribution = 'GGX'
    node_1.subsurface_method = 'RANDOM_WALK'

    node_2 = nodes.new('ShaderNodeTexGradient')
    node_2.name = 'Gradient Texture'
    node_2.location = (-657.7989501953125, 247.9912109375)
    node_2.width = 140.0
    node_2.width_hidden = 0.0
    node_2.height = 100.0
    node_2.label = ''
    node_2.use_custom_color = False
    node_2.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node_2.show_options = True
    node_2.show_preview = False
    node_2.hide = False
    node_2.mute = False
    node_2.show_texture = True
    node_2.bl_idname = 'ShaderNodeTexGradient'
    node_2.bl_label = 'Gradient Texture'
    node_2.bl_description = ''
    node_2.bl_icon = 'NONE'
    node_2.bl_static_type = 'TEX_GRADIENT'
    node_2.bl_width_default = 140.0
    node_2.bl_width_min = 100.0
    node_2.bl_width_max = 700.0
    node_2.bl_height_default = 100.0
    node_2.bl_height_min = 30.0
    node_2.bl_height_max = 30.0
    node_2.gradient_type = 'LINEAR'

    node_3 = nodes.new('ShaderNodeTexCoord')
    node_3.name = 'Texture Coordinate'
    node_3.location = (-915.0496826171875, 288.3238525390625)
    node_3.width = 140.0
    node_3.width_hidden = 0.0
    node_3.height = 100.0
    node_3.label = ''
    node_3.use_custom_color = False
    node_3.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node_3.show_options = True
    node_3.show_preview = False
    node_3.hide = False
    node_3.mute = False
    node_3.show_texture = False
    node_3.bl_idname = 'ShaderNodeTexCoord'
    node_3.bl_label = 'Texture Coordinate'
    node_3.bl_description = ''
    node_3.bl_icon = 'NONE'
    node_3.bl_static_type = 'TEX_COORD'
    node_3.bl_width_default = 140.0
    node_3.bl_width_min = 100.0
    node_3.bl_width_max = 700.0
    node_3.bl_height_default = 100.0
    node_3.bl_height_min = 30.0
    node_3.bl_height_max = 30.0
    node_3.from_instancer = False

    node_4 = nodes.new('ShaderNodeValToRGB')
    node_4.name = 'Color Ramp'
    node_4.location = (-369.2308044433594, 279.3607482910156)
    node_4.width = 240.0
    node_4.width_hidden = 0.0
    node_4.height = 100.0
    node_4.label = ''
    node_4.use_custom_color = False
    node_4.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node_4.show_options = True
    node_4.show_preview = False
    node_4.hide = False
    node_4.mute = False
    node_4.show_texture = False
    node_4.bl_idname = 'ShaderNodeValToRGB'
    node_4.bl_label = 'Color Ramp'
    node_4.bl_description = ''
    node_4.bl_icon = 'NONE'
    node_4.bl_static_type = 'VALTORGB'
    node_4.bl_width_default = 240.0
    node_4.bl_width_min = 140.0
    node_4.bl_width_max = 700.0
    node_4.bl_height_default = 100.0
    node_4.bl_height_min = 30.0
    node_4.bl_height_max = 30.0

    links.new(node_1.outputs['BSDF'], node_0.inputs['Surface'])
    links.new(node_3.outputs['Object'], node_2.inputs['Vector'])
    links.new(node_2.outputs['Color'], node_4.inputs['Fac'])
    links.new(node_4.outputs['Color'], node_1.inputs['Base Color'])

    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

apply_material_preset(bpy.context.active_object)