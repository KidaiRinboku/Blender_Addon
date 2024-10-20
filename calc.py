bl_info = {
    "name": "Dual Tab Calculator Add-on",
    "author": "KidaiRinboku",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "3D View > Sidebar > Item/View Tab",
    "description": "Adds a simple calculator to both Item and View tabs in the N-panel",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

import bpy
import math

def register_properties():
    bpy.types.Scene.calculator_input_item = bpy.props.StringProperty(
        name="Expression",
        description="Enter the expression",
        default="",
    )
    bpy.types.Scene.calculator_result_item = bpy.props.StringProperty(
        name="Result",
        description="Calculation result",
        default="",
    )
    bpy.types.Scene.calculator_input_view = bpy.props.StringProperty(
        name="Expression",
        description="Enter the expression",
        default="",
    )
    bpy.types.Scene.calculator_result_view = bpy.props.StringProperty(
        name="Result",
        description="Calculation result",
        default="",
    )

def unregister_properties():
    del bpy.types.Scene.calculator_input_item
    del bpy.types.Scene.calculator_result_item
    del bpy.types.Scene.calculator_input_view
    del bpy.types.Scene.calculator_result_view

class CALCULATOR_OT_calculate_item(bpy.types.Operator):
    bl_idname = "calculator.calculate_item"
    bl_label = "Calculate Item"

    def execute(self, context):
        scene = context.scene
        expression = scene.calculator_input_item

        try:
            allowed_names = {
                'abs': abs,
                'round': round,
                'min': min,
                'max': max,
                'math': math,
                '__builtins__': None,
            }
            result = eval(expression, {"__builtins__": None}, allowed_names)
            scene.calculator_result_item = str(result)
        except Exception:
            scene.calculator_result_item = "Error"

        return {'FINISHED'}

class CALCULATOR_OT_calculate_view(bpy.types.Operator):
    bl_idname = "calculator.calculate_view"
    bl_label = "Calculate View"

    def execute(self, context):
        scene = context.scene
        expression = scene.calculator_input_view

        try:
            allowed_names = {
                'abs': abs,
                'round': round,
                'min': min,
                'max': max,
                'math': math,
                '__builtins__': None,
            }
            result = eval(expression, {"__builtins__": None}, allowed_names)
            scene.calculator_result_view = str(result)
        except Exception:
            scene.calculator_result_view = "Error"

        return {'FINISHED'}

class ITEM_PT_calculator(bpy.types.Panel):
    bl_label = "Calculator"
    bl_idname = "ITEM_PT_calculator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_order = -1000

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "calculator_input_item", text="")
        row = layout.row()
        row.operator("calculator.calculate_item", text="=")
        row.prop(scene, "calculator_result_item", text="")

class VIEW_PT_calculator(bpy.types.Panel):
    bl_label = "Calculator"
    bl_idname = "VIEW_PT_calculator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    bl_order = -1000

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "calculator_input_view", text="")
        row = layout.row()
        row.operator("calculator.calculate_view", text="=")
        row.prop(scene, "calculator_result_view", text="")

def register():
    register_properties()
    bpy.utils.register_class(CALCULATOR_OT_calculate_item)
    bpy.utils.register_class(CALCULATOR_OT_calculate_view)
    bpy.utils.register_class(ITEM_PT_calculator)
    bpy.utils.register_class(VIEW_PT_calculator)

def unregister():
    bpy.utils.unregister_class(VIEW_PT_calculator)
    bpy.utils.unregister_class(ITEM_PT_calculator)
    bpy.utils.unregister_class(CALCULATOR_OT_calculate_view)
    bpy.utils.unregister_class(CALCULATOR_OT_calculate_item)
    unregister_properties()

if __name__ == "__main__":
    register()