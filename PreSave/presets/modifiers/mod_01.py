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
    mod.is_active = True
    mod.use_apply_on_spline = False
    mod.frame_start = 1.0
    mod.frame_duration = 10.0
    mod.use_reverse = False
    mod.use_random_order = False
    mod.seed = 0

for obj in bpy.context.selected_objects:
    apply_modifier_preset(obj)