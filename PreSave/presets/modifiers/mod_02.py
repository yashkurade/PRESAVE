import bpy

def apply_modifier_preset(obj):
    # Remove all existing modifiers
    for m in obj.modifiers:
        obj.modifiers.remove(m)

    mod = obj.modifiers.new(name='Build', type='BUILD')
    mod.show_viewport = True
    mod.show_render = True
    mod.show_in_editmode = False
    mod.show_on_cage = False
    mod.show_expanded = True
    mod.is_active = False
    mod.use_apply_on_spline = False
    mod.frame_start = 1.0
    mod.frame_duration = 10.0
    mod.use_reverse = False
    mod.use_random_order = False
    mod.seed = 0

    mod = obj.modifiers.new(name='Array', type='ARRAY')
    mod.show_viewport = True
    mod.show_render = True
    mod.show_in_editmode = True
    mod.show_on_cage = False
    mod.show_expanded = True
    mod.is_active = True
    mod.use_apply_on_spline = False
    mod.fit_type = 'FIXED_COUNT'
    mod.count = 5
    mod.fit_length = 0.0
    mod.curve = None
    mod.use_constant_offset = False
    mod.constant_offset_displace = Vector((1.0, 0.0, 0.0))
    mod.use_relative_offset = True
    mod.relative_offset_displace = Vector((2.3999998569488525, 0.0, 0.0))
    mod.use_merge_vertices = False
    mod.use_merge_vertices_cap = False
    mod.merge_threshold = 0.009999999776482582
    mod.use_object_offset = False
    mod.offset_object = None
    mod.start_cap = None
    mod.end_cap = None
    mod.offset_u = 0.0
    mod.offset_v = 0.0

for obj in bpy.context.selected_objects:
    apply_modifier_preset(obj)