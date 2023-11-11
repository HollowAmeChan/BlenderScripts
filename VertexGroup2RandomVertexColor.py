import bpy
import random
# 获取活动对象
obj = bpy.context.active_object
# 获取所有顶点组
vgroups = obj.vertex_groups



bpy.ops.object.editmode_toggle()
for i in range(len(vgroups)):
    selected_vgroup = vgroups[i]

    # 检查顶点组是否存在
    if selected_vgroup is not None:
        # 获取网格数据
        mesh = obj.data

        # 选择指定名称的顶点组所属的网格
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_set_active(group=selected_vgroup.name)
        bpy.ops.object.vertex_group_select()
        bpy.ops.object.mode_set(mode='OBJECT')
        # 赋予颜色
        bpy.ops.paint.vertex_paint_toggle()
        bpy.context.object.data.use_paint_mask = True 
        bpy.data.brushes["Draw"].color = (random.random(),random.random(),random.random())
        bpy.ops.paint.vertex_color_set()
        bpy.ops.object.editmode_toggle()

