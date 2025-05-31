import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class ApplyTransformPresetOperator(Operator, ImportHelper):
    """Apply Transform Preset"""
    bl_idname = "import_presets.apply_transform"
    bl_label = "Apply Transform Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def execute(self, context):
        try:
            with open(self.filepath, 'r') as f:
                code = f.read()
            exec(code, {'bpy': bpy})
            self.report({'INFO'}, "Preset applied successfully")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply preset: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}
