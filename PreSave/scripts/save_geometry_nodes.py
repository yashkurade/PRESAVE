import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator

class SaveGeometryNodesPresetOperator(Operator, ExportHelper):
    """Save Geometry Nodes Modifier Preset"""
    bl_idname = "export_presets.save_geometry_nodes"
    bl_label = "Save Geometry Nodes Preset"

    filename_ext = ".py"
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'})

    def invoke(self, context, event):
        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "No active object selected")
            return {'CANCELLED'}

        geom_mod = next((m for m in obj.modifiers if m.type == 'NODES'), None)
        if not geom_mod:
            self.report({'ERROR'}, "Active object has no Geometry Nodes modifier")
            return {'CANCELLED'}

        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        obj = context.active_object
        geom_mod = next((m for m in obj.modifiers if m.type == 'NODES'), None)
        if not geom_mod:
            self.report({'ERROR'}, "Active object has no Geometry Nodes modifier")
            return {'CANCELLED'}

        nt = geom_mod.node_group
        if not nt:
            self.report({'ERROR'}, "Geometry Nodes modifier has no node group")
            return {'CANCELLED'}

        lines = [
            "import bpy\n",
            "def apply_geometry_nodes_preset(obj):",
            "    for m in obj.modifiers:",
            "        if m.type == 'NODES':",
            "            obj.modifiers.remove(m)",
            "    mod = obj.modifiers.new(name='GeometryNodes', type='NODES')",
            "    ng = bpy.data.node_groups.new(name='GeometryNodesPreset', type='GeometryNodeTree')",
            "    mod.node_group = ng",
            "    nodes = ng.nodes",
            "    links = ng.links",
            "    nodes.clear()",
            "",
        ]

        # Save all nodes

        for node in nt.nodes:
            lines.append(f"    node = nodes.new('{node.bl_idname}')")
            lines.append(f"    node.name = '{node.name}'")
            lines.append(f"    node.location = ({node.location.x}, {node.location.y})")

            for prop in node.bl_rna.properties:
                if prop.identifier in {'name', 'location', 'select', 'width', 'height'}:
                    continue
                if prop.is_readonly or prop.is_hidden or getattr(prop, "is_pointer", False):
                    continue
                try:
                    val = getattr(node, prop.identifier)
                except:
                    continue
                if isinstance(val, (int, float, str, bool)):
                    val_repr = f"'{val}'" if isinstance(val, str) else repr(val)
                    lines.append(f"    node.{prop.identifier} = {val_repr}")

            # Save input socket default values
            for i, socket in enumerate(node.inputs):
                if not socket.is_linked and hasattr(socket, "default_value"):
                    val = socket.default_value
                    if isinstance(val, (float, int, bool)):
                        lines.append(f"    node.inputs[{i}].default_value = {val}")
                    elif isinstance(val, str):
                        lines.append(f"    node.inputs[{i}].default_value = '{val}'")
                    elif isinstance(val, (list, tuple)) or hasattr(val, '__iter__'):
                        # Likely color or vector input
                        lines.append(f"    node.inputs[{i}].default_value = {tuple(val)}")
                lines.append("")

        # Add safe linking function
        lines.append("    def safe_link(from_node_name, from_socket_name, to_node_name, to_socket_name):")
        lines.append("        from_node = nodes.get(from_node_name)")
        lines.append("        to_node = nodes.get(to_node_name)")
        lines.append("        if from_node and to_node:")
        lines.append("            out_socket = next((s for s in from_node.outputs if s.name == from_socket_name), None)")
        lines.append("            in_socket = next((s for s in to_node.inputs if s.name == to_socket_name), None)")
        lines.append("            if out_socket and in_socket:")
        lines.append("                links.new(out_socket, in_socket)")
        lines.append("")

        # Save links using safe_link()
        for link in nt.links:
            lines.append(f"    safe_link('{link.from_node.name}', '{link.from_socket.name}', '{link.to_node.name}', '{link.to_socket.name}')")

        lines.append("")
        lines.append("for obj in bpy.context.selected_objects:")
        lines.append("    apply_geometry_nodes_preset(obj)")

        try:
            with open(self.filepath, 'w') as f:
                f.write("\n".join(lines))
            self.report({'INFO'}, f"Geometry Nodes preset saved to: {self.filepath}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save preset: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}
