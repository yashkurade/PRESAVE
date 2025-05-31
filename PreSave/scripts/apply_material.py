import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class ApplyMaterialPresetOperator(Operator, ImportHelper):
    """Apply Material Preset"""
    bl_idname = "import_presets.apply_material"
    bl_label = "Apply Material Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def execute(self, context):
        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "No active object selected")
            return {'CANCELLED'}

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                script = f.read()

            namespace = {}
            exec(script, namespace)

            if "apply_material_preset" in namespace:
                namespace["apply_material_preset"](obj)
                self.report({'INFO'}, f"Material preset applied to '{obj.name}'")
            else:
                self.report({'ERROR'}, "Function 'apply_material_preset' not found in preset file")
                return {'CANCELLED'}

        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply material preset: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
