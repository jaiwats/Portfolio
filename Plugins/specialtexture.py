
bl_info = {
    "name": "Shader Library",
    "author": "Nano",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Shader",
}



import bpy
import bmesh 
import random
from random import randint



class NewPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Element Textures"
    bl_idname = "OBJECT_PT_Texture"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Element textures'
    
   
   
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Simple Fire")
        row.operator('shader.diamond_operator')
        
        row = layout.row()
        row.label(text="Energy")
        row.operator('shader.emrald_operator')
        
        
        row = layout.row()
        row.label(text="Liquid Shader")
        row.operator('shader.saphire_operator')
        
        row = layout.row()
        row.label(text="Random Shapes")
        row.operator('shader.ruby_operator')
    
        
    
class SimpleFire_Texture(bpy.types.Operator):
    bl_label = "Simple Fire"
    bl_idname = 'shader.diamond_operator'
    
    def execute(self, context):
        
        material_SimpleFire = bpy.data.materials.new(name= "SimpleFire")
        material_SimpleFire.use_nodes = True
        
        material_SimpleFire.node_tree.nodes.remove(material_SimpleFire.node_tree.nodes.get('Principled BSDF'))
    
        material_output = material_SimpleFire.node_tree.nodes.get('Material Output')
        material_output.location = (400,0)
    
    
        glass_node = material_SimpleFire.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node.location = (200,0)
        glass_node.inputs[0].default_value = (0, 0, 0, 1)
    
    
        Emission_node = material_SimpleFire.node_tree.nodes.new('ShaderNodeEmission')
        Emission_node.location = (200,-200)
        Emission_node.inputs[1].default_value = 10
    
        Brick_node = material_SimpleFire.node_tree.nodes.new('ShaderNodeTexBrick')
        Brick_node.location = (0,-100)
        Brick_node.inputs[1].default_value = (1, 0, 0, 1)
        Brick_node.inputs[2].default_value = (1, 0.089, 0, 1)
        Brick_node.inputs[3].default_value = (1, 0.2, 0, 1)
    
        material_SimpleFire.node_tree.links.new(glass_node.outputs[0], 
material_output.inputs[0])
    
        material_SimpleFire.node_tree.links.new(Brick_node.outputs[0], 
Emission_node.inputs[0])
    
        material_SimpleFire.node_tree.links.new(Emission_node.outputs[0], 
material_output.inputs[1])
    
        bpy.context.object.active_material = material_SimpleFire
        
        return {'FINISHED'}
    
    
    
    
        
class Energy_Texture(bpy.types.Operator):
    bl_label = "Energy"
    bl_idname = 'shader.emrald_operator'
    
    def execute(self, context):
        
        material_Energy = bpy.data.materials.new(name= "Energy")
        material_Energy.use_nodes = True
        
        material_Energy.node_tree.nodes.remove(material_Energy.node_tree.nodes.get('Principled BSDF'))
    
        material_output = material_Energy.node_tree.nodes.get('Material Output')
        material_output.location = (400,0)
    
    
        Emission_node = material_Energy.node_tree.nodes.new('ShaderNodeEmission')
        Emission_node.location = (200,-200)
        Emission_node.inputs[1].default_value = 10
    
        Brick_node = material_Energy.node_tree.nodes.new('ShaderNodeTexBrick')
        Brick_node.location = (0,-100)
        Brick_node.inputs[1].default_value = (0.2, 1, 0, 1)
        Brick_node.inputs[2].default_value = (0, 1, 0, 1)
        Brick_node.inputs[3].default_value = (0.5, 1, 0, 1)
    
    
        material_Energy.node_tree.links.new(Brick_node.outputs[0], 
Emission_node.inputs[0])
    
        material_Energy.node_tree.links.new(Emission_node.outputs[0], 
material_output.inputs[1])
    
        bpy.context.object.active_material = material_Energy
        
        return {'FINISHED'}
                
        
class WaterShader_Texture(bpy.types.Operator):
    bl_label = "Water Shader"
    bl_idname = 'shader.saphire_operator'
    
    def execute(self, context):
        
        material_WaterShader = bpy.data.materials.new(name= "WaterShader")
        material_WaterShader.use_nodes = True
        
        material_WaterShader.node_tree.nodes.remove(material_WaterShader.node_tree.nodes.get('Principled BSDF'))
    
        material_output = material_WaterShader.node_tree.nodes.get('Material Output')
        material_output.location = (400,0)
    
    
        glass_node_Cyan = material_WaterShader.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node_Cyan.location = (0,400)
        glass_node_Cyan.inputs[0].default_value = (0.189, 0.891, 1, 1)
        
        glass_node_Blue = material_WaterShader.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node_Blue.location = (0,300)
        glass_node_Blue.inputs[0].default_value = (0, 0, 1, 1)
        glass_node_Blue.inputs[2].default_value = 4.35
        
        glass_node_White = material_WaterShader.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node_White.location = (0,200)
        glass_node_White.inputs[0].default_value = (1, 1, 1, 1)
        
        glass_node_Blue_C = material_WaterShader.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass_node_Blue_C.location = (0,100)
        glass_node_Blue_C.inputs[0].default_value = (0, 0.117, 1, 1)
        glass_node_Blue_C.inputs[2].default_value = 4.35
        
        Mix_Shader_1 = material_WaterShader.node_tree.nodes.new('ShaderNodeMixShader')
        Mix_Shader_1.location = (100,350)
        
        
        Mix_Shader_2 = material_WaterShader.node_tree.nodes.new('ShaderNodeMixShader')
        Mix_Shader_2.location = (100,150)
        
        
        Mix_Shader_3 = material_WaterShader.node_tree.nodes.new('ShaderNodeMixShader')
        Mix_Shader_3.location = (200,0)
        
        Brick_Texture = material_WaterShader.node_tree.nodes.new('ShaderNodeTexBrick')
        Brick_Texture.location = (200,-200)
        Brick_Texture.inputs[1].default_value = (0, 0, 0, 1)
        Brick_Texture.inputs[2].default_value = (0, 0, 0, 1)
        Brick_Texture.inputs[3].default_value = (1, 1, 1, 1)
        Brick_Texture.inputs[4].default_value = 0
        Brick_Texture.inputs[8].default_value = 20.5
       
    
        material_WaterShader.node_tree.links.new(glass_node_Cyan.outputs[0], 
Mix_Shader_1.inputs[1])
    
        material_WaterShader.node_tree.links.new(glass_node_Blue.outputs[0], 
Mix_Shader_1.inputs[2])
    
        material_WaterShader.node_tree.links.new(glass_node_White.outputs[0], 
Mix_Shader_2.inputs[1])
    
        material_WaterShader.node_tree.links.new(glass_node_Blue_C.outputs[0], 
Mix_Shader_2.inputs[2])
        
        material_WaterShader.node_tree.links.new(Mix_Shader_1.outputs[0], 
Mix_Shader_3.inputs[1])
    
        material_WaterShader.node_tree.links.new(Mix_Shader_2.outputs[0], 
Mix_Shader_3.inputs[2])

        material_WaterShader.node_tree.links.new(Mix_Shader_3.outputs[0], 
material_output.inputs[0])

        material_WaterShader.node_tree.links.new(Brick_Texture.outputs[0], 
material_output.inputs[2])
    
        bpy.context.object.active_material = material_WaterShader
        
        return {'FINISHED'}   


   
class RandomShapeManipulator(bpy.types.Operator):
    bl_label = "Ranom Selector"
    bl_idname = 'shader.ruby_operator'
    
    def execute(self, context):
        min = 0
        max = 2
        myobj = bpy.context.active_object 
        bpy.ops.object.mode_set(mode='EDIT')
        
        faces_to_select = 30
        bpy.ops.mesh.select_all(action='DESELECT')
        
        mesh = bpy.context.object.data
        bm = bmesh.from_edit_mesh(mesh)
        
        faces_pool = bm.faces[:]
        for face_idx in range(faces_to_select):
            if not faces_pool:
                break
            if len(faces_pool) == 1:
                select_face = faces_pool.pop(0)
            else:
                select_face = faces_pool.pop(randint(0, len(faces_pool) - 1))
            select_face.select_set(True)
            for face in set(f for v in select_face.verts for f in v.link_faces if f in faces_pool):
                faces_pool.remove(face)
                
        bmesh.update_edit_mesh(mesh)
           
        
        return {'FINISHED'}
        
        
    


def register():
    bpy.utils.register_class(NewPanel)
    bpy.utils.register_class(SimpleFire_Texture)
    bpy.utils.register_class(Energy_Texture)
    bpy.utils.register_class(WaterShader_Texture)
    bpy.utils.register_class(RandomShapeManipulator)
def unregister():
    bpy.utils.unregister_class(NewPanel)
    bpy.utils.unregister_class(SimpleFire_Texture)
    bpy.utils.unregister_class(Energy_Texture)
    bpy.utils.unregister_class(WaterShader_Texture)
    bpy.utils.unregister_class(RandomShapeManipulator)


if __name__ == "__main__":
    register()
