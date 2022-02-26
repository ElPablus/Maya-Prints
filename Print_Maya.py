import maya.cmds as cmds
import maya.mel as mel
import os


def run(*args):

    fname = cmds.file(query=True, sceneName=True)
    filename = os.path.basename(fname)
    raw_name, extension = os.path.splitext(filename)
    filepath, namefile = os.path.split(fname)
    files_folder= os.listdir(filepath)
    files_maya = [i for i in files_folder if i.endswith('.ma')]

    size= cmds.radioButtonGrp('Type_File',query= True, select=True)
    if size == 1:
        with_photo= 1000
        height_photo= 800
    else:
        with_photo= 1134
        height_photo= 1416

    for files_print in files_maya:

        camera_angle= cmds.floatField('angle_value',query=True, value=True)*-1
        zoom_camera = cmds.floatField('angle_value', query=True, value=True)
        menucamera= cmds.optionMenu('option_camera_view', query=True, value=True)
        name, fin= os.path.splitext(files_print)
        completeFName= (filepath +('/'+ name+ '.jpg'))

    
        
        file_open= cmds.file('%s\%s.ma' %(filepath,name),o=True, type='mayaAscii',iv=True, pr=True, f=1)
        
        cmds.select('persp')
        cmds.move(54,60,47)
        cmds.rotate(camera_angle,45,0)
        currentCam = cmds.lookThru(q=True)
        cmdStr = "lookThroughModelPanel" + " " + "persp" + " " + "modelPanel4;"
        mel.eval(cmdStr)
        cmds.lookThru(menucamera)
        cmds.select(all=True,hi=True)
        geoa= cmds.ls(sl=1, type='mesh', dag=1, ni=1)
        cmds.select(geoa)
        cmds.viewFit(f=zoom_camera)
        cmds.select(clear=True)
        print(name)
        cameras_ui()
        cmds.setAttr ('defaultRenderGlobals.imageFormat' ,8)
        cmds.playblast(st= 1, et= 1, v= False,os= False, format= 'image', quality= 100, percent= 100, width= with_photo, height= height_photo, framePadding= 0, cf= completeFName)


def example(*args):

    fname = cmds.file(query=True, sceneName=True)
    filename = os.path.basename(fname)
    raw_name, extension = os.path.splitext(filename)
    filepath, namefile = os.path.split(fname)
    files_folder= os.listdir(filepath)
    files_maya = [i for i in files_folder if i.endswith('.ma')]

    camera_angle= cmds.floatField('angle_value',query=True, value=True)*-1
    zoom_camera = cmds.floatField('zoom_value', query=True, value=True)
    menucamera= cmds.optionMenu('option_camera_view', query=True, value=True)
    name= raw_name

    completeFName= (filepath +('/'+ name+ '.jpg'))
    size= cmds.radioButtonGrp('Type_File',query= True, select=True)
    if size == 1:
        with_photo= 1000
        height_photo= 800
    else:
        with_photo= 1134
        height_photo= 1416
    
    cmds.select('persp')
    cmds.move(54,60,47)
    cmds.rotate(camera_angle,45,0)
    currentCam = cmds.lookThru(q=True)
    cmdStr = "lookThroughModelPanel" + " " + "persp" + " " + "modelPanel4;"
    mel.eval(cmdStr)
    cmds.lookThru(menucamera)
    cmds.select(all=True,hi=True)
    geoa= cmds.ls(sl=1, type='mesh', dag=1, ni=1)
    cmds.select(geoa)
    cmds.viewFit(f=zoom_camera)
    cmds.select(clear=True)
    
    cameras_ui()
    cmds.setAttr ('defaultRenderGlobals.imageFormat' ,8)
    cmds.playblast(st= 1, et= 1, v= False, format= 'image', quality= 100, percent= 100, width= with_photo, height= height_photo, framePadding= 0, cf= completeFName)
    print(name)


def cameras_ui():
    panels= cmds.getPanel( all=True )
    namepa= cmds.getPanel( type='modelPanel' )
    for hidepanel in namepa:
        cmds.modelEditor(hidepanel,e= True, hud= False, grid= False,nurbsCurves= False,displayTextures=True)

def enable_angle(*args):
    option_angle_mn= cmds.optionMenu('option_camera_view', query=True, value=True)
    if option_angle_mn == 'persp':
        cmds.floatField('angle_value',edit=True, editable=True)
        
    else:
        cmds.floatField('angle_value',edit=True, editable=False)


def size_miniature(*args):
    size= cmds.radioButtonGrp('Type_File',query= True, select=True)
    if size == 1:
        with_photo= 1000
        height_photo= 800
    else:
        with_photo= 800
        height_photo= 1000
    

