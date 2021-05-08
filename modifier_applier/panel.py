import bpy

from bpy.types import Panel


class TOM_ADDON_PT_PANEL(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Modifier operations"
    bl_category = "Tom Util"

    def draw(self, context):
        layout = self.layout

        row = layout.row()

        col = layout.column()
        col.operator(
            "object.apply_all_mods",
            text='Apply all'
        ).action = 'apply'

        col = layout.column()
        col.operator(
            "object.apply_all_mods",
            text='Cancel all'
        ).action = 'cancel'
