import bpy

class PresetManagerPanel(bpy.types.Panel):
    bl_label = "PreSave"
    bl_idname = "VIEW3D_PT_preset_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PresSave'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Select a preset category below:")

class PresetManagerPanelTransform(bpy.types.Panel):
    bl_label = "Transform Presets"
    bl_parent_id = "VIEW3D_PT_preset_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PreSave'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        obj = context.active_object

        layout.prop(scene, "save_location")
        layout.prop(scene, "save_rotation")
        layout.prop(scene, "save_scale")
        layout.prop(scene, "save_full_animation", text="Save Full Animation")

        save_enabled = obj and (scene.save_location or scene.save_rotation or scene.save_scale)

        row = layout.row()
        row.enabled = save_enabled
        row.operator("export_presets.save_transform", text="Save Transform Preset", icon="EXPORT")

        row = layout.row()
        row.operator("import_presets.apply_transform", text="Apply Transform Preset", icon="IMPORT")

class PresetManagerPanelModifiers(bpy.types.Panel):
    bl_label = "Modifier Presets"
    bl_parent_id = "VIEW3D_PT_preset_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PreSave'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        save_enabled = obj is not None and len(obj.modifiers) > 0

        row = layout.row()
        row.enabled = save_enabled
        row.operator("export_presets.save_modifier", text="Save Modifier Preset", icon="EXPORT")

        row = layout.row()
        row.operator("import_presets.apply_modifier", text="Apply Modifier Preset", icon="IMPORT")

class PresetManagerPanelMaterial(bpy.types.Panel):
    bl_label = "Material Presets"
    bl_parent_id = "VIEW3D_PT_preset_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PreSave'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        layout.label(text="Only active material will be saved")

        if not obj:
            layout.label(text="No object selected", icon='ERROR')
            return
        if not obj.active_material:
            layout.label(text="No active material", icon='INFO')
        
        # Save button (enabled only if there is a material)
        row = layout.row()
        row.enabled = obj.active_material is not None
        row.operator("export_presets.save_material", text="Save Material Preset", icon="EXPORT")

        # Apply button (always enabled)
        layout.operator("import_presets.apply_material", text="Apply Material Preset", icon="IMPORT")

class PresetManagerPanelGeometryNodes(bpy.types.Panel):
    bl_label = "Geometry Nodes Presets"
    bl_parent_id = "VIEW3D_PT_preset_manager"  # Same parent as others
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PreSave'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        has_geo_nodes = False

        if obj:
            # Check if the object has a Geometry Nodes modifier
            for mod in obj.modifiers:
                if mod.type == 'NODES':
                    has_geo_nodes = True
                    break

        row = layout.row()
        row.enabled = has_geo_nodes
        row.operator("export_presets.save_geometry_nodes", text="Save Geometry Nodes Preset", icon="EXPORT")

        row = layout.row()
        row.operator("import_presets.apply_geometry_nodes", text="Apply Geometry Nodes Preset", icon="IMPORT")
