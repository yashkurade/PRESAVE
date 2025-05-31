import bpy

def apply_transform(obj):
    data = {'location': [(1, (0.0, 0.0, 0.0)), (60, (-8.02, 0.0, 0.0))], 'scale': [(1, (1.0, 1.0, 1.0)), (60, (1.0, 1.0, 1.0))]}

    for prop, keyframes in data.items():
        for frame, value in keyframes:
            setattr(obj, prop, value)
            obj.keyframe_insert(data_path=prop, frame=frame)

for obj in bpy.context.selected_objects:
    apply_transform(obj)
