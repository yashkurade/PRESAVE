import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator

class SaveTransformPresetOperator(Operator, ExportHelper):
    """Save Transform Preset"""
    bl_idname = "export_presets.save_transform"
    bl_label = "Save Transform Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        obj = context.active_object
        scene = context.scene

        if not obj:
            self.report({'ERROR'}, "No active object selected")
            return {'CANCELLED'}

        save_animation = scene.save_full_animation
        include_location = scene.save_location
        include_rotation = scene.save_rotation
        include_scale = scene.save_scale

        if not any([include_location, include_rotation, include_scale]):
            self.report({'ERROR'}, "Select at least one transform component to save.")
            return {'CANCELLED'}

        if not save_animation:
            # Static values
            lines = ["import bpy", "", "def apply_transform(obj):"]
            if include_location:
                loc = tuple(round(v, 4) for v in obj.location)
                lines.append(f"    obj.location = {loc}")
            if include_rotation:
                rot = tuple(round(v, 4) for v in obj.rotation_euler)
                lines.append(f"    obj.rotation_euler = {rot}")
            if include_scale:
                scale = tuple(round(v, 4) for v in obj.scale)
                lines.append(f"    obj.scale = {scale}")

            lines.append("")
            lines.append("for obj in bpy.context.selected_objects:")
            lines.append("    apply_transform(obj)")

            script = "\n".join(lines)
        else:
            action = obj.animation_data.action if obj.animation_data else None

            if not action:
                self.report({'WARNING'}, "No animation data found. Saving static values instead.")
                return self.execute_static(context)  # fallback

            # Get all keyframes
            frames = set()
            for fcurve in action.fcurves:
                for keyframe_point in fcurve.keyframe_points:
                    frames.add(int(keyframe_point.co.x))
            frames = sorted(frames)

            # Collect data per transform type
            data = {}
            if include_location:
                data['location'] = [(f, tuple(round(v, 4) for v in self.get_value(obj, f, 'location'))) for f in frames]
            if include_rotation:
                data['rotation_euler'] = [(f, tuple(round(v, 4) for v in self.get_value(obj, f, 'rotation_euler'))) for f in frames]
            if include_scale:
                data['scale'] = [(f, tuple(round(v, 4) for v in self.get_value(obj, f, 'scale'))) for f in frames]

            script = f"""import bpy

def apply_transform(obj):
    data = {data}

    for prop, keyframes in data.items():
        for frame, value in keyframes:
            setattr(obj, prop, value)
            obj.keyframe_insert(data_path=prop, frame=frame)

for obj in bpy.context.selected_objects:
    apply_transform(obj)
"""

        try:
            with open(self.filepath, 'w') as f:
                f.write(script)
            self.report({'INFO'}, f"Transform preset saved to: {self.filepath}")
        except Exception as e:
            self.report({'ERROR'}, f"Could not save file: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

    def get_value(self, obj, frame, attr):
        bpy.context.scene.frame_set(frame)
        return getattr(obj, attr)
