import bpy
from bpy.types import Operator


class MESH_GEN_OT_OP(Operator):
    bl_idname = "object.do_action"
    bl_label = "Do"
    bl_description = "Do this"

    action = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active

        return {'FINISHED'}
