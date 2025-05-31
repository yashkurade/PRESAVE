import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator

class SaveModifierPresetOperator(Operator, ExportHelper):
    """Save Modifier Preset"""
    bl_idname = "export_presets.save_modifier"
    bl_label = "Save Modifier Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def invoke(self, context, event):
        if not context.active_object:
            self.report({'ERROR'}, "No active object selected")
            return {'CANCELLED'}
        if not context.active_object.modifiers:
            self.report({'ERROR'}, "Active object has no modifiers")
            return {'CANCELLED'}

        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        obj = context.active_object

        if not obj:
            self.report({'ERROR'}, "No active object selected")
            return {'CANCELLED'}

        modifiers_data = []

        for mod in obj.modifiers:
            mod_data = {
                "name": mod.name,
                "type": mod.type,
                "properties": {}
            }

            # Iterate over all RNA properties for this modifier
            for prop in mod.bl_rna.properties:
                # Skip read-only, pointer properties, and 'name' (we handle name separately)
                if prop.is_readonly:
                    continue
                if getattr(prop, "is_pointer", False):
                    continue
                if prop.identifier == "name":
                    continue

                try:
                    value = getattr(mod, prop.identifier)
                    # Some properties may not be serializable or cause errors, so skip them safely
                    mod_data["properties"][prop.identifier] = value
                except Exception as e:
                    print(f"Skipped property {prop.identifier} due to error: {e}")

            modifiers_data.append(mod_data)

        # Build Python script text that recreates the modifiers on selected objects
        script_lines = [
            "import bpy\n",
            "def apply_modifier_preset(obj):",
            "    # Remove all existing modifiers",
            "    for m in obj.modifiers:",
            "        obj.modifiers.remove(m)",
            "",
        ]

        for mod in modifiers_data:
            script_lines.append(f"    mod = obj.modifiers.new(name='{mod['name']}', type='{mod['type']}')")
            for key, val in mod["properties"].items():
                # Format strings with quotes, numbers as is, booleans as is
                if isinstance(val, str):
                    val_repr = f"'{val}'"
                else:
                    val_repr = repr(val)
                script_lines.append(f"    mod.{key} = {val_repr}")
            script_lines.append("")  # blank line for readability

        script_lines.append("for obj in bpy.context.selected_objects:")
        script_lines.append("    apply_modifier_preset(obj)")

        script = "\n".join(script_lines)

        try:
            with open(self.filepath, 'w') as f:
                f.write(script)
            self.report({'INFO'}, f"Modifier preset saved to: {self.filepath}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save preset: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}
