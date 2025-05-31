import bpy

def apply_transform(obj):
    data = {'location': [(1, (0.0, 0.0, 0.0)), (60, (-2.71, -2.64, 1.8))], 'rotation_euler': [(1, (0.0, 0.0, 0.0)), (60, (1.9373, -1.0472, 1.7104))], 'scale': [(1, (1.0, 1.0, 1.0)), (60, (0.16, 1.15, 1.78))]}

    for t in ['location', 'rotation_euler', 'scale']:
        for frame, value in data[t]:
            setattr(obj, t, value)
            obj.keyframe_insert(data_path=t, frame=frame)

for obj in bpy.context.selected_objects:
    apply_transform(obj)
