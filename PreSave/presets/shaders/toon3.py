import bpy
from mathutils import Color

def apply_material_preset(obj):
    mat = bpy.data.materials.new(name='shaded_dir.001')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    node = nodes.new('ShaderNodeOutputMaterial')
    node.name = 'Material Output'
    node.location = (300.0, 300.0)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeBsdfPrincipled')
    node.name = 'Principled BSDF'
    node.location = (-944.8446044921875, 378.2276306152344)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeShaderToRGB')
    node.name = 'Shader to RGB'
    node.location = (-479.5250549316406, 322.2612609863281)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeValToRGB')
    node.name = 'Color Ramp'
    node.location = (-101.53520202636719, 353.9610900878906)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    links.new(nodes['Color Ramp'].outputs['Color'], nodes['Material Output'].inputs['Surface'])
    links.new(nodes['Principled BSDF'].outputs['BSDF'], nodes['Shader to RGB'].inputs['Shader'])
    links.new(nodes['Shader to RGB'].outputs['Color'], nodes['Color Ramp'].inputs['Fac'])

    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
