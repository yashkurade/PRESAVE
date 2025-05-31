import bpy

def apply_transform(obj):
    obj.location = (0.0, 0.0, 0.0)

for obj in bpy.context.selected_objects:
    apply_transform(obj)