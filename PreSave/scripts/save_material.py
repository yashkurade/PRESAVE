import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator

class SaveMaterialPresetOperator(Operator, ExportHelper):
    """Save Material Preset"""
    bl_idname = "export_presets.save_material"
    bl_label = "Save Material Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def execute(self, context):
        obj = context.active_object
        mat = obj.active_material if obj else None

        if not mat:
            self.report({'ERROR'}, "Active object has no material")
            return {'CANCELLED'}

        try:
            lines = [
                "import bpy",
                "from mathutils import Color",
                "",
                "def apply_material_preset(obj):",
                "    mat = bpy.data.materials.new(name='{}')".format(mat.name),
                "    mat.use_nodes = True",
                "    nodes = mat.node_tree.nodes",
                "    links = mat.node_tree.links",
                "    nodes.clear()",
                ""
            ]

            for node in mat.node_tree.nodes:
                lines.append("    node = nodes.new('{}')".format(node.bl_idname))
                lines.append("    node.name = '{}'".format(node.name))
                lines.append("    node.location = {}".format(tuple(node.location)))
                lines.append("    node.label = '{}'".format(node.label))
                if hasattr(node, "color"):
                    lines.append("    node.color = Color({})".format(tuple(node.color)))
                lines.append("")

            for link in mat.node_tree.links:
                from_node = link.from_node.name
                from_socket = link.from_socket.name
                to_node = link.to_node.name
                to_socket = link.to_socket.name
                lines.append(f"    links.new(nodes['{from_node}'].outputs['{from_socket}'], nodes['{to_node}'].inputs['{to_socket}'])")

            lines.append("")
            lines.append("    if obj.data.materials:")
            lines.append("        obj.data.materials[0] = mat")
            lines.append("    else:")
            lines.append("        obj.data.materials.append(mat)")
            lines.append("")

            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write("\n".join(lines))

            self.report({'INFO'}, f"Material preset saved to: {self.filepath}")
            return {'FINISHED'}

        except Exception as e:
            self.report({'ERROR'}, f"Could not save file: {e}")
            return {'CANCELLED'}
