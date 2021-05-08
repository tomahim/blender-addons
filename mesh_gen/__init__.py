import bpy

from .panel import MESH_GEN_PT_PANEL
from .op import MESH_GEN_OT_OP

bl_info = {
    "name": "Mesh gen",
    "author": "Tomahim",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "View 3D"
}


classes = [MESH_GEN_PT_PANEL, MESH_GEN_OT_OP]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
