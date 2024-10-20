bl_info = {
    "name": "3lines",
    "author": "KidaiRinboku",
    "version": (1, 6),
    "blender": (2, 80, 0),
    "location": "N side menu->Item adn View",
    "description": "add 3 lines text field to Item and View N side menu",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

import bpy
from bpy.props import StringProperty

def register_properties():
    bpy.types.Scene.custom_text_field_1 = StringProperty(
        name="",
        description="line1",
        default=""
    )
    bpy.types.Scene.custom_text_field_2 = StringProperty(
        name="",
        description="line2",
        default=""
    )
    bpy.types.Scene.custom_text_field_3 = StringProperty(
        name="",
        description="line3",
        default=""
    )

def unregister_properties():
    del bpy.types.Scene.custom_text_field_1
    del bpy.types.Scene.custom_text_field_2
    del bpy.types.Scene.custom_text_field_3

#item_pannel
class ITEM_PT_custom_text_field(bpy.types.Panel):
    bl_label = ""
    bl_idname = "ITEM_PT_custom_text_field"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'  
    bl_options = {'HIDE_HEADER'}
    bl_order = 9999

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "custom_text_field_1", text="")
        layout.prop(scene, "custom_text_field_2", text="")
        layout.prop(scene, "custom_text_field_3", text="")

#view_pannel
class VIEW_PT_custom_text_field(bpy.types.Panel):
    bl_label = ""
    bl_idname = "VIEW_PT_custom_text_field"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View' 
    bl_options = {'HIDE_HEADER'}
    bl_order = 9999

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "custom_text_field_1", text="")
        layout.prop(scene, "custom_text_field_2", text="")
        layout.prop(scene, "custom_text_field_3", text="")

def register():
    register_properties()
    bpy.utils.register_class(ITEM_PT_custom_text_field)
    bpy.utils.register_class(VIEW_PT_custom_text_field)

def unregister():
    unregister_properties()
    bpy.utils.unregister_class(VIEW_PT_custom_text_field)
    bpy.utils.unregister_class(ITEM_PT_custom_text_field)

if __name__ == "__main__":
    register()