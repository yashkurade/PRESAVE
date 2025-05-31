import bpy

def apply_transform(obj):
    obj.location = (-1.9869, -1.9356, 1.3197)
    obj.rotation_euler = (1.4204, -0.7678, 1.254)
    obj.scale = (0.3841, 1.11, 1.5719)

for obj in bpy.context.selected_objects:
    apply_transform(obj)
