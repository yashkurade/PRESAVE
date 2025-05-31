import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class ApplyModifierPresetOperator(Operator, ImportHelper):
    """Apply Modifier Preset"""
    bl_idname = "import_presets.apply_modifier"
    bl_label = "Apply Modifier Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        try:
            # Read the preset script text
            with open(self.filepath, 'r') as f:
                script = f.read()

            # Execute the preset script in a safe namespace
            exec(script, {"bpy": bpy})

            self.report({'INFO'}, f"Modifier preset applied from: {self.filepath}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply preset: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}
