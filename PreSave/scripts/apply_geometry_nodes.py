import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class ApplyGeometryNodesPresetOperator(Operator, ImportHelper):
    """Apply Geometry Nodes Modifier Preset"""
    bl_idname = "import_presets.apply_geometry_nodes"
    bl_label = "Apply Geometry Nodes Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        try:
            with open(self.filepath, 'r') as f:
                script = f.read()

            # Execute the saved script in global namespace so it can run apply_geometry_nodes_preset()
            exec(script, {"bpy": bpy})

            self.report({'INFO'}, f"Geometry Nodes preset applied from: {self.filepath}")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply preset: {e}")
            return {'CANCELLED'}
