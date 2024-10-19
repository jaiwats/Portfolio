
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

#This is the start of the code

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
                
        

    
    
 


def register():
    bpy.utils.register_class(NewPanel)
    bpy.utils.register_class(SimpleFire_Texture)
    bpy.utils.register_class(Energy_Texture)

def unregister():
    bpy.utils.unregister_class(NewPanel)
    bpy.utils.unregister_class(SimpleFire_Texture)
    bpy.utils.unregister_class(Energy_Texture)


if __name__ == "__main__":
    register()
