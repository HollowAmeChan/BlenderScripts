```
修复mmdtools/cat的导入骨骼，相连项的bug
有一些骨骼莫名其妙的打开了相连项，导致导入vdp表情/姿态会产生很多骨骼移动不了的bug
解决办法是关掉相连项
```


import bpy
#首先需要选择到所有的骨骼
arm = bpy.context.selected_bones
for i in arm:
    if i.use_connect == 1:
        bpy.types.EditBone(i).use_connect = 0
