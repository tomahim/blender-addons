import bpy
from bpy.types import Operator


class MESH_GEN_OT_OP(Operator):
    bl_idname = "object.do_action"
    bl_label = "Do"
    bl_description = "Add array modifier"

    action = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True
        # return context.object is not None and context.object.mode == "OBJECT"

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        if self.action == 'add_modifier':
            self._add_modifier(active_obj)
        if self.action == 'create_curve':
            self._create_curve(active_obj)
        if self.action == 'to_mesh':
            self._to_mesh(active_obj)
        return {'FINISHED'}

    def _add_modifier(self, active_obj):
        mod = active_obj.modifiers.new(
            name="array2",
            type="ARRAY"
        )
        mod.count = 5
        mod.relative_offset_displace.x = 1.0

    def _create_curve(self, active_obj):
        # sample data
        coords = [(1, 0, 1), (2, 0, 0), (3, 0, 1), (4, 0, 0), (5, 0, 1)]

        # create the Curve Datablock
        curveData = bpy.data.curves.new('myCurve', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 2

        # map coords to spline
        polyline = curveData.splines.new('POLY')
        polyline.points.add(len(coords)-1)
        for i, coord in enumerate(coords):
            x, y, z = coord
            polyline.points[i].co = (x, y, z, 1)

        # create Object
        curveOB = bpy.data.objects.new('myCurve', curveData)
        curveData.bevel_depth = 0.2

        # attach to scene and validate context
        scn = bpy.context.scene
        scn.collection.objects.link(curveOB)
        bpy.context.view_layer.objects.active = curveOB

        # convert curve to mesh
        curveOB.select_set(True)
        bpy.ops.object.convert(target='MESH')
