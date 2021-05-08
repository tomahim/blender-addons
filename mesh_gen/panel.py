import bpy
from bpy.types import Panel


class MESH_GEN_PT_PANEL(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Mesh Gen"
    bl_category = "Mesh Gen Tom"

    def draw(self, context):
        layout = self.layout

        row = layout.row()

        col = layout.column()
        col.operator(
            "object.do_action",
            text='Do this'
        ).action = 'apply'
