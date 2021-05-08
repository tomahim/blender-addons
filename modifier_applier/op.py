import bpy
from bpy.types import Operator


class TOM_ADDON_OT_Apply_All_OP(Operator):
    bl_idname = "object.apply_all_mods"
    bl_label = "Apply all"
    bl_description = "Apply all operators of active object"

    action = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        if self.action == 'apply':
            for mod in active_obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=mod.name)
        if self.action == 'cancel':
            active_obj.modifiers.clear()

        return {'FINISHED'}
