bl_info = {
    "name": "PreSave",
    "author": "YashK.",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > PreSave",
    "description": "Save and apply presets",
    "category": "Object",
}

import bpy
from . import ui_panel
from .scripts import save_transform, apply_transform, save_modifier, apply_modifier, save_material, apply_material, save_geometry_nodes, apply_geometry_nodes

classes = [
    save_transform.SaveTransformPresetOperator,
    apply_transform.ApplyTransformPresetOperator,
    save_modifier.SaveModifierPresetOperator,
    apply_modifier.ApplyModifierPresetOperator,
    save_material.SaveMaterialPresetOperator,
    apply_material.ApplyMaterialPresetOperator,
    save_geometry_nodes.SaveGeometryNodesPresetOperator,
    apply_geometry_nodes.ApplyGeometryNodesPresetOperator,
    ui_panel.PresetManagerPanel,
    ui_panel.PresetManagerPanelTransform,
    ui_panel.PresetManagerPanelModifiers,
    ui_panel.PresetManagerPanelMaterial,
    ui_panel.PresetManagerPanelGeometryNodes,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Scene properties for saving
    bpy.types.Scene.save_full_animation = bpy.props.BoolProperty(
        name="Save Full Animation",
        description="Save all keyframes for location, rotation, and scale",
        default=False,
    )
    bpy.types.Scene.save_location = bpy.props.BoolProperty(
        name="Location",
        description="Include Location in the preset",
        default=True,
    )
    bpy.types.Scene.save_rotation = bpy.props.BoolProperty(
        name="Rotation",
        description="Include Rotation in the preset",
        default=True,
    )
    bpy.types.Scene.save_scale = bpy.props.BoolProperty(
        name="Scale",
        description="Include Scale in the preset",
        default=True,
    )

def unregister():
    del bpy.types.Scene.save_full_animation
    del bpy.types.Scene.save_location
    del bpy.types.Scene.save_rotation
    del bpy.types.Scene.save_scale

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
