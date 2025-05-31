import bpy
from mathutils import Color

def apply_material_preset(obj):
    mat = bpy.data.materials.new(name='testo3434')
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
    node.location = (10.0, 300.0)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeTexGradient')
    node.name = 'Gradient Texture'
    node.location = (-657.7989501953125, 247.9912109375)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeTexCoord')
    node.name = 'Texture Coordinate'
    node.location = (-915.0496826171875, 288.3238525390625)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    node = nodes.new('ShaderNodeValToRGB')
    node.name = 'Color Ramp'
    node.location = (-369.2308044433594, 279.3607482910156)
    node.label = ''
    node.color = Color((0.6079999804496765, 0.6079999804496765, 0.6079999804496765))

    links.new(nodes['Principled BSDF'].outputs['BSDF'], nodes['Material Output'].inputs['Surface'])
    links.new(nodes['Texture Coordinate'].outputs['Object'], nodes['Gradient Texture'].inputs['Vector'])
    links.new(nodes['Gradient Texture'].outputs['Color'], nodes['Color Ramp'].inputs['Fac'])
    links.new(nodes['Color Ramp'].outputs['Color'], nodes['Principled BSDF'].inputs['Base Color'])

    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
