```
基于mmdtools，使用了那边的导入vpd
用于将mmd模型中的vpd表情骨骼姿态，转化为形态键
适合做vrc模使用
脚本的folder_path填入vpd表情文件夹

使用脚本前先导出一份默认姿态的vpd，烘焙完后，再导入默认姿态的vpd，不进行这个操作的话，模型烘焙完会停留在最后一个表情回不去了（这个脚本没有使用到姿态库）
首先选择好模型的骨架，运行脚本
```


import bpy
import os

def get_all_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def get_first_children_mesh(obj):
    for i in obj.children:
        if i.type == 'MESH':
            return i
        
def get_first_armature(obj):
    for i in obj.modifiers:
        if i.type == 'ARMATURE':
            return i    
#---------------------------------------------------------
#需要填入自己的参数
folder_path = "D:\\尻尻文件\\(魔)コハル\\(魔)コハル\\表情\\"
scale = 0.08
#---------------------------------------------------------

all_files = get_all_files_in_folder(folder_path)
arm = bpy.context.active_object

#获取骨架的第一个网格
mesh = get_first_children_mesh(arm)
#获取网格的第一个骨架修改器
mdf = get_first_armature(mesh)
    
for path in all_files:
#path = all_files[10]

    name = os.path.basename(path)
    trueName = os.path.splitext(name)[0]
    #导入vpd姿态
    print(path)
    print(name)
    bpy.ops.mmd_tools.import_vpd(filepath=path, files=[{"name":name, "name":name}], directory=folder_path, scale=scale)
    #从mesh的骨架修改器上应用形态键
    bpy.context.active_object.select_set(False)
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier=mdf.name)
    #对应用的形态键改名为vpd姿态名
    mesh.data.shape_keys.key_blocks[mdf.name].name = trueName

    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.posemode_toggle()
    bpy.context.active_object.select_set(True)
    




