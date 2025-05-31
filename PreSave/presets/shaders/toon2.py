import bpy
from mathutils import Color

def apply_material_preset(obj):
    mat = bpy.data.materials.new(name='shaded_dir.001')
    mat.use_nodes = True
    obj.active_material = mat
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    node = nodes.new('ShaderNodeOutputMaterial')
    node.name = 'Material Output'
    node.location = (300.0, 300.0)
    node.label = ''
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'ShaderNodeOutputMaterial'
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
    node.location = (-944.8446044921875, 378.2276306152344)
    node.label = ''
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'ShaderNodeBsdfPrincipled'
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
    node = nodes.new('ShaderNodeShaderToRGB')
    node.name = 'Shader to RGB'
    node.location = (-479.5250549316406, 322.2612609863281)
    node.label = ''
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.select = False
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'ShaderNodeShaderToRGB'
    node.bl_label = 'Shader to RGB'
    node.bl_description = ''
    node.bl_icon = 'NONE'
    node.bl_static_type = 'SHADERTORGB'
    node.bl_width_default = 140.0
    node.bl_width_min = 100.0
    node.bl_width_max = 700.0
    node.bl_height_default = 100.0
    node.bl_height_min = 30.0
    node.bl_height_max = 30.0
    node = nodes.new('ShaderNodeValToRGB')
    node.name = 'Color Ramp'
    node.location = (-101.53520202636719, 353.9610900878906)
    node.label = ''
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.width_hidden = 0.0
    node.height = 100.0
    node.label = ''
    node.parent = None
    node.use_custom_color = False
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))
    node.select = True
    node.show_options = True
    node.show_preview = False
    node.hide = False
    node.mute = False
    node.show_texture = False
    node.bl_idname = 'ShaderNodeValToRGB'
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
    node.color_ramp.elements.clear()
    elt = node.color_ramp.elements.new(0.0)
    elt.color = (0.05448022112250328, 0.028425980359315872, 0.08650043606758118, 1.0)
    elt = node.color_ramp.elements.new(0.050999999046325684)
    elt.color = (0.3005436658859253, 0.10461631417274475, 0.19806931912899017, 1.0)
    elt = node.color_ramp.elements.new(0.3633897006511688)
    elt.color = (0.8387991189956665, 0.23455023765563965, 0.15592654049396515, 1.0)
    elt = node.color_ramp.elements.new(0.9545455574989319)
    elt.color = (0.8468732237815857, 0.4178846478462219, 0.2663556933403015, 1.0)
    # Recreate links
    links.new(nodes['Color Ramp'].outputs['Color'], nodes['Material Output'].inputs['Surface'])
    links.new(nodes['Principled BSDF'].outputs['BSDF'], nodes['Shader to RGB'].inputs['Shader'])
    links.new(nodes['Shader to RGB'].outputs['Color'], nodes['Color Ramp'].inputs['Fac'])

for obj in bpy.context.selected_objects:
    apply_material_preset(obj)