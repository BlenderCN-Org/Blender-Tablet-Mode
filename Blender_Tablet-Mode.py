### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Tablet Mode",
    "author": "Matthias Ellerbeck",
    "version": (0, 0, 2),
    "blender": (2, 76, 0),
    "location": "Node Editor",
    "description": "Enables a Tablet Mode for Blender",
    "warning": "Early development state!",
    "wiki_url": "",
    "category": "User Interface",
    }
    
import bpy

#main operator
class MouseClickModalOperator(bpy.types.Operator):
    bl_idname = "wm.tabletmode"
    bl_label = "Activate Tablet Mode"

    def modal(self, context, event):
        if event.is_tablet != True: #Ignoring all non-tablet events
            return{'PASS_THROUGH'}
        if context.area.type == 'NODE_EDITOR': #Does not work, gives back 'USER_PREFERENCES' every time
            print("Yay!")
            return{'PASS_THROUGH'}
        return{'RUNNING_MODAL'}
    
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

#adding buttons for common used functions
def NodeEditorPanel(self,context):
    layout = self.layout
    col = layout.column()
    row = col.row(align=True)

    row.alignment = 'CENTER'
    row.operator("bpy.ops.node.delete()", icon="X", text="Delete") #Delete button, currently doesn't work

#registration
def register():
    #bpy.utils.register_module(__name__)
    bpy.utils.register_class(MouseClickModalOperator)
    bpy.types.NODE_HT_header.append(NodeEditorPanel)

def unregister():
    #bpy.utils.unregister_module(__name__)
    bpy.utils.unregister_class(MouseClickModalOperator)
    bpy.types.NODE_HT_header.remove(NodeEditorPanel)

if __name__ == "__main__":
    register()
    #bpy.ops.wm.tabletmode('INVOKE_SCREEN')