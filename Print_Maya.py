import time
import maya.cmds as cmds
import maya.mel as mel
import os

def example(*args):

    fname =cmds.file(query=True, l=True)[0]
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
        with_photo= 2000
        height_photo= 2000
    else:
        with_photo= 600
        height_photo= 600
    
    cmds.select('persp')
    cmds.move(54,60,47)
    cmds.rotate(camera_angle,45,0)
    currentCam = cmds.lookThru(q=True)
    cmdStr = "lookThroughModelPanel" + " " + "persp" + " " + "modelPanel4;"
    mel.eval(cmdStr)
    cmds.lookThru(menucamera)
    cmds.select(all=True,hi=True)
    geoa= cmds.ls(sl=1, type='mesh', dag=1, ni=1, visible=True)
    cmds.select(geoa)
    cmds.viewFit()
    cmds.select(clear=True)
    cmds.camera('front', edit=True, orthographicWidth= 72.295+ zoom_camera*5)
    cmds.camera('persp', edit=True, focalLength= 35 + zoom_camera*5)
    cmds.camera('front', edit=True, focalLength= 35 + zoom_camera)
    cameras_ui()
    
    cmds.setAttr ('defaultRenderGlobals.imageFormat' ,8)
    cmds.playblast(st= 1, et= 1, v= False,os= False, format= 'image', quality= 100, percent= 100, width= with_photo, height= height_photo, framePadding= 0, cf= completeFName)
    cmds.camera('persp', edit=True, focalLength= 35)
    cmds.camera('front', edit=True, focalLength= 35)

def cameras_ui():
    panels= cmds.getPanel( all=True )
    namepa= cmds.getPanel( type='modelPanel' )
    for hidepanel in namepa:
        cmds.modelEditor(hidepanel,e= True, hud= False, grid= False,nurbsCurves= False,displayTextures=True,wireframeOnShaded=False,polymeshes=True,displayAppearance='smoothShaded')

def enable_angle(*args):
    option_angle_mn= cmds.optionMenu('option_camera_view', query=True, value=True)
    if option_angle_mn == 'persp':
        cmds.floatField('angle_value',edit=True, editable=True)
        
    else:
        cmds.floatField('angle_value',edit=True, editable=False)


def Run_run(*args):
    
    fname = cmds.file(query=True, l=True)[0]
    filename = os.path.basename(fname)
    raw_name, extension = os.path.splitext(filename)
    filepath, namefile = os.path.split(fname)
    files_folder= os.listdir(filepath)
    files_maya = [i for i in files_folder if i.endswith('.ma')]
    len_bar= len(files_maya)
    count=0
    size= cmds.radioButtonGrp('Type_File',query= True, select=True)
    amount = 0
    sumante= 100/len_bar
    if size == 1:
        with_photo= 2000
        height_photo= 2000
    else:
        with_photo= 600
        height_photo= 600
        
    cmds.progressWindow(title='Waiting',progress=amount,status='Progress: 0%',isInterruptable=True )
    while count < len_bar :
        
        camera_angle= cmds.floatField('angle_value',query=True, value=True)*-1
        zoom_camera = cmds.floatField('zoom_value', query=True, value=True)
        menucamera= cmds.optionMenu('option_camera_view', query=True, value=True)
        name_f=files_maya[count]
        sl= name_f.split('.')
        name= sl[0]
        completeFName= (filepath +('/'+ name+ '.jpg'))
       
        
        
        file_open= cmds.file('%s\%s.ma' %(filepath,name),o=True, type='mayaAscii',iv=True, pr=True, f=1)
        
        cmds.warning('file '+ name +' is opened')
       
        cmds.select('persp')
        cmds.move(54,60,47)
        cmds.rotate(camera_angle,45,0)
        currentCam = cmds.lookThru(q=True)  
        cmdStr = "lookThroughModelPanel" + " " + "persp" + " " + "modelPanel4;"
        mel.eval(cmdStr)
        cmds.lookThru(menucamera)
        cmds.select(all=True,hi=True)
        geoa= cmds.ls(sl=1, type='mesh', dag=1, ni=1, visible=True)
        cmds.select(geoa)
        cmds.viewFit()
        cmds.select(clear=True)
        cmds.camera('front', edit=True, orthographicWidth= 72.295+ zoom_camera*5)
        cmds.camera('persp', edit=True, focalLength= 35 + zoom_camera*5)
        cmds.camera('front', edit=True, focalLength= 35 + zoom_camera)
        
        cameras_ui()
        
        cmds.setAttr ('defaultRenderGlobals.imageFormat' ,8)
        cmds.playblast(st= 1, et= 1, v= False,os= False, format= 'image', quality= 100, percent= 100, width= with_photo, height= height_photo, framePadding= 0, cf= completeFName)
        cmds.warning('capture comlete')
        cmds.camera('persp', edit=True, focalLength= 35)
        cmds.camera('front', edit=True, focalLength= 35)

        cmds.warning('path file:'+ completeFName)
        amount= amount+ sumante
        count= count+1
        
        time.sleep(5)
        
        if cmds.progressWindow(query=True, isCancelled=True ) :
            cmds.warning('Interrumpido')
            break

        # Check if end condition has been reached
        if cmds.progressWindow(query=True, progress=True ) >= 100 :
            cmds.warning('Finalizado')
            break
        
        cmds.progressWindow(edit=True, progress=amount, status=('Sleeping: ' + str(amount) + '%' ) )
    cmds.progressWindow(endProgress=1)
