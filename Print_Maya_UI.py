import maya.cmds as cmds
import Print_Maya
reload(Print_Maya)

interface = 'Maya_Print'
title_name = 'Maya_Prints'
w_interface = 300
h_interface = 50
def lunch_ui():
    if cmds.window(interface, query = True, exists = True):
        cmds.deleteUI(interface)
    cmds.window(interface)
    cmds.window(interface, edit = True, w= w_interface + 2, h=h_interface,title= title_name, mnb= True, mxb= False, s=False )
    
    cmds.columnLayout('title_layout', w = w_interface, )
    
    create_customUI()
    
    cmds.showWindow(interface)

def create_customUI():
    cmds.rowLayout('first_line',nc=4, w=w_interface, p= 'title_layout')
    cmds.text('text_camara_view',label='Camera',w=w_interface/4)
    cmds.optionMenu('option_camera_view', w= w_interface/4, cc= Print_Maya.enable_angle)
    cmds.menuItem( label='front' )
    cmds.menuItem( label='persp' )
    cmds.text('text_zoom',label='Zoom',w=w_interface/4)
    cmds.floatField('zoom_value',minValue= -25 , maxValue= 100,precision=2,w= w_interface/4, editable=True)
    
    cmds.separator(p='title_layout', height=5, style='in')
        
    cmds.rowLayout('second_line',nc=3, w=w_interface, p= 'title_layout')
    cmds.text('text_angle',label='Angle',w=w_interface/4)
    cmds.floatField('angle_value',minValue= 0 , maxValue= 90,precision=2,w= w_interface/4,editable=False)
    cmds.radioButtonGrp('Type_File',cw2=(65,65), labelArray2=['Print', 'Icon'], numberOfRadioButtons=2, w=w_interface/2,select=1)

    cmds.separator(p='title_layout', height=5, style='in')

    cmds.rowLayout('last_line',nc=3, w=w_interface, p= 'title_layout')
    cmds.button(l='Start',w= w_interface/2, c=Print_Maya.Run_run)
    cmds.button(l='Example',w= w_interface/2, c=Print_Maya.example)
    #cmds.button(l='sample',w= w_interface/3, c=Print_Maya.example_bar)

lunch_ui()